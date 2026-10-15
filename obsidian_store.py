from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="Obsidian Smart Spaces | S-Prime AI")

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OBSIDIAN | Catálogo Smart Spaces</title>
        <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
        <style>
            :root { 
                --bg-dark: #050505; 
                --obsidian-red: #ff003c; 
                --obsidian-glow: rgba(255, 0, 60, 0.4);
            }
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Rajdhani', sans-serif; }
            body { background: var(--bg-dark); color: #fff; padding: 50px; }
            
            .header { text-align: center; margin-bottom: 50px; }
            .header h1 { font-size: 3rem; color: #fff; text-shadow: 0 0 20px var(--obsidian-glow); text-transform: uppercase; }
            .header p { color: #888; font-size: 1.2rem; letter-spacing: 2px; text-transform: uppercase; }
            
            .product-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto; }
            
            .product-card { 
                background: #0a0a0a; border: 1px solid #222; border-radius: 8px; padding: 20px; 
                transition: 0.3s; position: relative; overflow: hidden;
            }
            .product-card:hover { border-color: var(--obsidian-red); box-shadow: 0 0 25px var(--obsidian-glow); transform: translateY(-5px); }
            
            .badge { position: absolute; top: 15px; right: 15px; background: var(--obsidian-red); color: #fff; padding: 5px 10px; font-size: 0.8rem; font-weight: bold; border-radius: 4px; }
            
            .product-img-placeholder { height: 200px; background: #111; border: 1px dashed #333; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; border-radius: 4px; color: #555; }
            
            .product-title { font-size: 1.4rem; margin-bottom: 10px; color: #fff; }
            .product-desc { font-size: 0.9rem; color: #aaa; margin-bottom: 20px; line-height: 1.4; }
            .product-price { font-size: 1.5rem; color: var(--obsidian-red); font-weight: bold; margin-bottom: 20px; }
            
            .btn-buy { 
                width: 100%; background: transparent; border: 1px solid var(--obsidian-red); color: var(--obsidian-red); 
                padding: 12px; font-size: 1.1rem; font-weight: bold; border-radius: 4px; cursor: pointer; transition: 0.3s; text-transform: uppercase; 
            }
            .btn-buy:hover { background: var(--obsidian-red); color: #fff; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>OBSIDIAN SMART SPACES</h1>
            <p>// Manufactura 3D On-Demand & Setup Táctico</p>
        </div>

        <div class="product-grid">
            <!-- Producto 1 -->
            <div class="product-card">
                <div class="badge">ON-DEMAND</div>
                <div class="product-img-placeholder">[RENDER: Relicario Sukuna]</div>
                <h3 class="product-title">Soporte PS5: El Relicario</h3>
                <p class="product-desc">Santuario demoníaco hiperdetallado diseñado milimétricamente para sostener mandos de consola. Impresión 3D en resina oscura.</p>
                <div class="product-price">$45.00 USD</div>
                <button class="btn-buy" onclick="alert('Conectando con Craftcloud/Impresora Local...')">Fabricar & Enviar</button>
            </div>

            <!-- Producto 2 -->
            <div class="product-card">
                <div class="badge">BEST SELLER</div>
                <div class="product-img-placeholder">[RENDER: Busto Gojo LED]</div>
                <h3 class="product-title">Stand Audífonos: Vacío Púrpura</h3>
                <p class="product-desc">Busto minimalista con integración de iluminación LED violeta hacia la diadema de los audífonos.</p>
                <div class="product-price">$60.00 USD</div>
                <button class="btn-buy">Fabricar & Enviar</button>
            </div>

            <!-- Producto 3 -->
            <div class="product-card">
                <div class="badge">TECH</div>
                <div class="product-img-placeholder">[RENDER: MagSafe Sharingan]</div>
                <h3 class="product-title">Cargador MagSafe: Tsukuyomi</h3>
                <p class="product-desc">Placa táctica de carga inalámbrica. Textura de metal oscuro con iluminación LED roja reactiva a la carga.</p>
                <div class="product-price">$35.00 USD</div>
                <button class="btn-buy">Fabricar & Enviar</button>
            </div>

            <!-- Producto 4 -->
            <div class="product-card">
                <div class="badge">ON-DEMAND</div>
                <div class="product-img-placeholder">[RENDER: Organizador Jinwoo]</div>
                <h3 class="product-title">Organizador: Ejército de Sombras</h3>
                <p class="product-desc">Gestor de escritorio para USBs y stylus. Diseño de fantasía oscura urbana con detalles en morado fluorescente.</p>
                <div class="product-price">$40.00 USD</div>
                <button class="btn-buy">Fabricar & Enviar</button>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8040)
