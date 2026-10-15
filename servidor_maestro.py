from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import sqlite3
import stripe

app = FastAPI(title="S-PRIME VÓRTEX Core - Rango S")

# Inicializar base de datos
db_path = "kinetic.db"
con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS licencias (
        key TEXT PRIMARY KEY,
        status TEXT,
        user_id TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
con.commit()
con.close()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_path = "templates/index.html"
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>S-PRIME CORP - Rango S Operativo</h1>"

@app.get("/health")
def health_check():
    return {"status": "healthy", "corporacion": "S-Prime Kinetic Corp", "rango": "S"}

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request, stripe_signature: str = Header(None)):
    payload = await request.body()
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

    if not webhook_secret:
        return {"status": "error", "message": "Missing webhook secret configuration"}

    try:
        event = stripe.Webhook.construct_event(payload, stripe_signature, webhook_secret)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid Stripe signature: {str(e)}")

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session.get('id', 'desconocido')
        customer_email = session.get('customer_details', {}).get('email', 'cliente@s-primecorp.com')
        
        try:
            con = sqlite3.connect("kinetic.db")
            cur = con.cursor()
            license_key = f"SPRIME-{order_id[-8:].upper()}"
            cur.execute("INSERT OR IGNORE INTO licencias (key, status, user_id) VALUES (?, ?, ?)", (license_key, "active", customer_email))
            con.commit()
            con.close()
        except Exception as e:
            print(f"Error BD: {e}")

    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8030)
