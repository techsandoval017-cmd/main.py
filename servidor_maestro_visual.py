import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(title="S-Prime Kinetic Corp")

# Habilitar la carpeta 'static' para leer tus imágenes
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>S-PRIME KINETIC CORP</title>
        <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
        <style>
            :root { 
                --kinetic-green: #39ff14;
                --obsidian-red: #ff003c;
            }
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Rajdhani', sans-serif; }
            body { background-color: #000; color: #fff; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }
            
            nav { height: 60px; background-color: #050505; display: flex; justify-content: space-between; align-items: center; padding: 0 40px; border-bottom: 1px solid #1a1a1a; }
            .nav-links { display: flex; gap: 25px; text-transform: uppercase; font-size: 0.8rem; font-weight: 600; color: #888; letter-spacing: 1.5px; }
            .btn-nav-login { border: 1px solid var(--obsidian-red); color: var(--obsidian-red); background: transparent; padding: 6px 20px; font-weight: bold; border-radius: 4px; text-transform: uppercase; cursor: pointer; }
            
            .main-container { display: flex; flex: 1; height: calc(100vh - 60px); }

            /* PANEL KINETIC (VERDE) */
            .panel-kinetic { flex: 1; padding: 40px 50px; display: flex; flex-direction: column; border-right: 1px solid rgba(57,255,20,0.3); background: radial-gradient(circle at top left, #0a1f0a 0%, #000 80%); }
            .panel-kinetic h1 { font-size: 3rem; margin-bottom: 5px; text-shadow: 0 0 20px rgba(57,255,20,0.4); }
            
            .btn-free-pdf { border: 1px dashed var(--kinetic-green); background: transparent; color: var(--kinetic-green); padding: 10px 20px; border-radius: 4px; margin-bottom: 20px; cursor: pointer; }
            .btn-reto { background: rgba(0,0,0,0.6); border: 2px solid var(--kinetic-green); color: #fff; padding: 15px 30px; font-size: 1.4rem; font-weight: bold; border-radius: 8px; margin-bottom: 25px; cursor: pointer; }
            
            .tiers-container { display: flex; gap: 15px; }
            .tier-box { flex: 1; border: 1px solid var(--kinetic-green); background: rgba(0,0,0,0.6); padding: 20px; border-radius: 8px; }
            .tier-box h3 { font-size: 1.8rem; color: var(--kinetic-green); }

            /* PANEL OBSIDIAN (ROJO) */
            .panel-obsidian { flex: 1; padding: 40px 50px; display: flex; flex-direction: column; align-items: center; text-align: center; background: radial-gradient(circle at center, #1a0005 0%, #000 80%); }
            
            /* AQUÍ VA TU LOGO 3D REAL DE OBSIDIAN */
            .logo-obsidian-real { height: 220px; margin-bottom: 20px; object-fit: contain; filter: drop-shadow(0 0 20px rgba(255,0,60,0.5)); }

            .panel-obsidian h1 { font-size: 3rem; margin-bottom: 5px; text-shadow: 0 0 20px rgba(255,0,60,0.4); }
            .btn-vortex { background: transparent; border: 2px solid var(--obsidian-red); color: #fff; padding: 18px 40px; font-size: 1.3rem; font-weight: bold; border-radius: 8px; margin-bottom: 20px; cursor: pointer; }
        </style>
    </head>
    <body>
        <nav>
            <!-- AQUÍ VA TU LOGO REAL DE LA BARRA DE NAVEGACIÓN -->
            <img src="/static/logo_nav.png" alt="S-Prime Corp" style="height: 40px;" onerror="this.src=''; this.alt='[FALTA SUBIR logo_nav.png A LA CARPETA static]'; this.style.color='red';">
            
            <div class="nav-links">
                <span>Menu</span><span>About App</span><span>Entrenamiento</span><span>Primes</span><span>Resources</span><span>Contact</span>
            </div>
            <button class="btn-nav-login">Solicitar Acceso</button>
        </nav>

        <div class="main-container">
            <div class="panel-kinetic">
                <h1>S-PRIME KINETIC</h1>
                <h2 style="color: #a0a0a0; margin-bottom: 25px;">// ACADEMIA DE NIVELACIÓN B2B</h2>
                <button class="btn-free-pdf">📄 RECURSOS Y PDFS GRATUITOS</button>
                <button class="btn-reto">TIER 1: EL RETO LEVEL 7 | $69 MXN</button>
                <div class="tiers-container">
                    <div class="tier-box"><h3>TIER 2</h3><p>Oficios Técnicos.</p></div>
                    <div class="tier-box"><h3>TIER 3</h3><p>Golden Suites.</p></div>
                </div>
            </div>

            <div class="panel-obsidian">
                <!-- AQUÍ VA TU ESCUDO 3D REAL -->
                <img src="/static/logo_obsidian.png" alt="Escudo Obsidian" class="logo-obsidian-real" onerror="this.src=''; this.alt='[FALTA SUBIR logo_obsidian.png A LA CARPETA static]'; this.style.color='red'; this.style.fontSize='20px';">
                
                <h1>OBSIDIAN S-PRIME</h1>
                <h2 style="color: #a0a0a0; margin-bottom: 30px;">// SOFTWARE DE ÉLITE NADA MÁS</h2>
                <button class="btn-vortex">SOLICITAR ACCESO AL VÓRTICE</button>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8030)
