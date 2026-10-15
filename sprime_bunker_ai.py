from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(title="S-Prime Corp | Búnker AI")

# Montar la carpeta static para cargar los fondos de los personajes
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>S-PRIME AI | Mando Central</title>
        <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
        <style>
            :root { 
                /* Colores base por defecto (Itachi - Rango S) */
                --theme-color: #ff003c;
                --theme-glow: rgba(255, 0, 60, 0.4);
                --bg-overlay: rgba(5, 7, 10, 0.85); /* Oscurece el fondo para que el texto se lea */
            }
            
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Rajdhani', sans-serif; }
            
            body { 
                color: #e0e0e0; 
                display: flex; 
                height: 100vh; 
                overflow: hidden;
                background-color: #000;
            }

            /* Contenedor del Fondo Dinámico */
            #dynamic-bg {
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                z-index: -2;
                transition: background-image 0.5s ease-in-out;
            }

            /* Filtro oscuro sobre la imagen de fondo */
            #bg-filter {
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: linear-gradient(to right, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.7) 100%);
                z-index: -1;
            }
            
            /* BARRA LATERAL - EL GREMIO */
            .sidebar { 
                width: 280px; 
                background: rgba(0, 0, 0, 0.6); 
                backdrop-filter: blur(10px);
                border-right: 1px solid var(--theme-color); 
                display: flex; 
                flex-direction: column; 
                padding: 20px 0;
                transition: border-color 0.5s ease;
                z-index: 10;
            }
            .logo-area { text-align: center; padding-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px; }
            .logo-area h2 { color: #fff; font-size: 2rem; letter-spacing: 2px; text-shadow: 0 0 15px var(--theme-color); transition: text-shadow 0.5s; }
            .logo-area span { color: var(--theme-color); transition: color 0.5s ease; }
            
            .agent-list { flex: 1; overflow-y: auto; padding: 0 15px; }
            .agent-item { 
                display: flex; align-items: center; padding: 12px; 
                background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.1); 
                border-radius: 6px; margin-bottom: 10px; cursor: pointer; transition: 0.3s; 
            }
            .agent-item:hover { background: rgba(255,255,255,0.1); transform: translateX(5px); border-color: var(--theme-color); }
            
            .rank-badge { font-weight: bold; font-size: 1.5rem; margin-right: 15px; width: 30px; text-align: center; }
            .agent-info h4 { font-size: 1.1rem; color: #fff; }
            .agent-info p { font-size: 0.8rem; color: #aaa; text-transform: uppercase; }

            /* PANEL CENTRAL - TERMINAL */
            .main-panel { 
                flex: 1; display: flex; flex-direction: column; 
                background: transparent; 
                position: relative; 
            }
            
            .chat-header { 
                height: 70px; border-bottom: 1px solid rgba(255,255,255,0.1); 
                display: flex; align-items: center; padding: 0 30px; 
                background: rgba(0, 0, 0, 0.5); backdrop-filter: blur(5px);
            }
            .chat-header h3 { color: #fff; font-size: 1.4rem; display: flex; align-items: center; gap: 15px; text-transform: uppercase; letter-spacing: 1px; }
            .status-dot { width: 12px; height: 12px; background: var(--theme-color); border-radius: 50%; box-shadow: 0 0 15px var(--theme-glow); transition: 0.5s; }

            .chat-box { flex: 1; padding: 30px; overflow-y: auto; display: flex; flex-direction: column; gap: 20px; }
            .msg { max-width: 80%; padding: 15px 20px; border-radius: 8px; line-height: 1.5; font-size: 1.1rem; backdrop-filter: blur(5px); }
            
            .msg-ai { 
                background: rgba(0,0,0,0.7); 
                border: 1px solid var(--theme-color); 
                color: #e0e0e0; align-self: flex-start; 
                box-shadow: inset 0 0 20px rgba(0,0,0,0.8), 0 0 15px var(--theme-glow);
                transition: border-color 0.5s, box-shadow 0.5s;
            }
            .msg-user { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; align-self: flex-end; }

            .input-area { 
                padding: 20px 30px; background: rgba(0,0,0,0.8); 
                border-top: 1px solid var(--theme-color); display: flex; gap: 15px; 
                transition: border-color 0.5s;
            }
            .cmd-input { 
                flex: 1; background: rgba(0,0,0,0.5); border: 1px solid #333; 
                color: #fff; padding: 15px 20px; font-size: 1.1rem; border-radius: 6px; outline: none; transition: 0.3s; 
            }
            .cmd-input:focus { border-color: var(--theme-color); box-shadow: inset 0 0 10px var(--theme-glow); }
            .btn-send { 
                background: transparent; border: 2px solid var(--theme-color); 
                color: var(--theme-color); font-weight: bold; font-size: 1.1rem; padding: 0 30px; 
                border-radius: 6px; cursor: pointer; transition: 0.3s; text-transform: uppercase; 
            }
            .btn-send:hover { background: var(--theme-color); color: #000; box-shadow: 0 0 20px var(--theme-glow); }

        </style>
    </head>
    <body>
        
        <!-- FONDOS DINÁMICOS -->
        <div id="dynamic-bg" style="background-image: url('/static/itachi.jpg');"></div>
        <div id="bg-filter"></div>

        <!-- BARRA LATERAL: GREMIO DE AGENTES -->
        <div class="sidebar">
            <div class="logo-area">
                <h2>S-PRIME <span>AI</span></h2>
            </div>
            
            <div class="agent-list">
                <!-- S - Itachi -->
                <div class="agent-item" onclick="selectAgent('S', 'Itachi Uchiha', 'Tsukuyomi', '#ff003c', 'itachi.jpg')">
                    <div class="rank-badge" style="color: #ff003c;">S</div>
                    <div class="agent-info"><h4>Itachi Uchiha</h4><p>Orquestador / Élite</p></div>
                </div>
                <!-- A - Goku -->
                <div class="agent-item" onclick="selectAgent('A', 'Goku SSJ', 'Despertar Namek', '#ff9800', 'goku.jpg')">
                    <div class="rank-badge" style="color: #ff9800;">A</div>
                    <div class="agent-info"><h4>Goku SSJ</h4><p>Arquitecto / Código</p></div>
                </div>
                <!-- B - Jinwoo -->
                <div class="agent-item" onclick="selectAgent('B', 'Jinwoo Sung', 'Monarca de las Sombras', '#9c27b0', 'jinwoo.jpg')">
                    <div class="rank-badge" style="color: #9c27b0;">B</div>
                    <div class="agent-info"><h4>Jinwoo Sung</h4><p>Analista / Finanzas</p></div>
                </div>
                <!-- C - Gojo -->
                <div class="agent-item" onclick="selectAgent('C', 'Gojo Satoru', 'Vacío Inconmensurable', '#2196f3', 'gojo.jpg')">
                    <div class="rank-badge" style="color: #2196f3;">C</div>
                    <div class="agent-info"><h4>Gojo Satoru</h4><p>Soporte / Tutoría</p></div>
                </div>
                <!-- D - Rick -->
                <div class="agent-item" onclick="selectAgent('D', 'Rick Sanchez', 'Dimensión C-137', '#39ff14', 'rick.jpg')">
                    <div class="rank-badge" style="color: #39ff14;">D</div>
                    <div class="agent-info"><h4>Rick Sanchez</h4><p>Redactor / Científico</p></div>
                </div>
                <!-- E - Sukuna -->
                <div class="agent-item" onclick="selectAgent('E', 'Sukuna', 'Relicario Demoníaco', '#e0e0e0', 'sukuna.jpg')">
                    <div class="rank-badge" style="color: #e0e0e0;">E</div>
                    <div class="agent-info"><h4>Sukuna</h4><p>Recolector / Datos</p></div>
                </div>
            </div>
        </div>

        <!-- PANEL CENTRAL: TERMINAL -->
        <div class="main-panel">
            <div class="chat-header">
                <div class="status-dot"></div> 
                <h3 id="current-agent">ITACHI UCHIHA - RANGO S</h3>
            </div>
            
            <div class="chat-box" id="chat-box">
                <div class="msg msg-ai">
                    <strong style="color:var(--theme-color); font-size:1.2rem;">[S-Prime AI - Mando Central]:</strong><br><br>
                    Bienvenido al Búnker, Director. <br>
                    Estás conectado a la red. Selecciona a tu agente en el panel izquierdo para invocar su dominio y delegar tareas. <br>
                    ¿Qué imperio vamos a construir hoy?
                </div>
            </div>

            <div class="input-area">
                <input type="text" id="user-input" class="cmd-input" placeholder="Dale una orden al Gremio..." onkeypress="if(event.key === 'Enter') sendMessage()">
                <button class="btn-send" onclick="sendMessage()">Ejecutar</button>
            </div>
        </div>

        <script>
            // Función para cambiar todo el entorno visual al seleccionar un agente
            function selectAgent(rank, name, domain, color, bgImage) {
                // Cambiar variables CSS (Colores de neón, botones y bordes)
                document.documentElement.style.setProperty('--theme-color', color);
                
                // Opacidad del resplandor adaptada al color
                let rgb = hexToRgb(color);
                document.documentElement.style.setProperty('--theme-glow', `rgba(${rgb.r}, ${rgb.g}, ${rgb.b}, 0.5)`);
                
                // Cambiar el Fondo
                document.getElementById('dynamic-bg').style.backgroundImage = `url('/static/${bgImage}')`;
                
                // Cambiar Header
                document.getElementById('current-agent').innerText = `${name} - RANGO ${rank} (${domain})`;
                
                // Mensaje de invocación en el chat
                let chatBox = document.getElementById('chat-box');
                chatBox.innerHTML += `
                <div class="msg msg-ai">
                    <strong style="color:var(--theme-color);">[S-Prime AI - ${name}]:</strong><br>
                    Dominio [${domain}] expandido. Listo para procesar tus órdenes, Director.
                </div>`;
                chatBox.scrollTop = chatBox.scrollHeight;
            }

            // Convertir Hex a RGB para el resplandor
            function hexToRgb(hex) {
                var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
                return result ? {
                    r: parseInt(result[1], 16),
                    g: parseInt(result[2], 16),
                    b: parseInt(result[3], 16)
                } : {r: 255, g: 0, b: 60};
            }

            function sendMessage() {
                let input = document.getElementById('user-input');
                let chatBox = document.getElementById('chat-box');
                let text = input.value.trim();
                let currentAgent = document.getElementById('current-agent').innerText.split(' - ')[0];
                
                if(text !== "") {
                    chatBox.innerHTML += `<div class="msg msg-user"><strong>[Director]:</strong><br>${text}</div>`;
                    
                    setTimeout(() => {
                        chatBox.innerHTML += `
                        <div class="msg msg-ai">
                            <strong style="color:var(--theme-color);">[S-Prime AI - ${currentAgent}]:</strong><br>
                            Recibido. Procesando orden bajo mi dominio...
                        </div>`;
                        chatBox.scrollTop = chatBox.scrollHeight;
                    }, 600);
                    
                    input.value = "";
                    chatBox.scrollTop = chatBox.scrollHeight;
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8035)
