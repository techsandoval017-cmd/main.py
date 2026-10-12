import http.server
import socketserver
import json
import os
import urllib.request

PORT = 8080
API_KEY = os.environ.get("GEMINI_API_KEY", "")

HTML_PAGE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tech Sandoval - Centro de Control B2B</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen font-sans p-4 md:p-8">
  <div class="max-w-6xl mx-auto space-y-6">
    <!-- Header -->
    <header class="flex flex-col md:flex-row md:items-center justify-between border-b border-slate-800 pb-4 gap-4">
      <div>
        <h1 class="text-2xl font-bold tracking-tight text-sky-400">⚡ Tech Sandoval: Fábrica de Agentes B2B</h1>
        <p class="text-xs text-slate-400">Panel Operativo Local • Modo Seguro (Sin consumo de saldo externo)</p>
      </div>
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 bg-emerald-500/10 text-emerald-400 text-xs font-medium rounded-full border border-emerald-500/20">
          <span class="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          3 Agentes Activos (Local Mock)
        </span>
      </div>
    </header>

    <!-- Grid de Productos -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <!-- Producto 1 -->
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-5 hover:border-sky-500/40 transition">
        <div class="flex justify-between items-start mb-2">
          <span class="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 bg-sky-500/10 text-sky-400 rounded border border-sky-500/20">eCommerce</span>
          <span class="text-xs font-semibold text-emerald-400">$297 - $597 USD</span>
        </div>
        <h2 class="font-semibold text-sm text-white mb-1">Bot WhatsApp + Shopify</h2>
        <p class="text-xs text-slate-400 mb-3 leading-relaxed">Venta conversacional, verificación de stock y generación de checkout directo.</p>
        <div class="text-[11px] text-slate-500 border-t border-slate-800/80 pt-2 flex justify-between">
          <span>Estado:</span>
          <span class="text-emerald-400 font-mono">LISTO LOCAL</span>
        </div>
      </div>

      <!-- Producto 2 -->
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-5 hover:border-amber-500/40 transition">
        <div class="flex justify-between items-start mb-2">
          <span class="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 bg-amber-500/10 text-amber-400 rounded border border-amber-500/20">Servicios</span>
          <span class="text-xs font-semibold text-emerald-400">$197 - $497 USD</span>
        </div>
        <h2 class="font-semibold text-sm text-white mb-1">Citas Barbería Anti-Ausentismo</h2>
        <p class="text-xs text-slate-400 mb-3 leading-relaxed">Agenda interactiva por WhatsApp con recordatorios 24h/2h y confirmación.</p>
        <div class="text-[11px] text-slate-500 border-t border-slate-800/80 pt-2 flex justify-between">
          <span>Estado:</span>
          <span class="text-emerald-400 font-mono">LISTO LOCAL</span>
        </div>
      </div>

      <!-- Producto 3 -->
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-5 hover:border-purple-500/40 transition">
        <div class="flex justify-between items-start mb-2">
          <span class="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 bg-purple-500/10 text-purple-400 rounded border border-purple-500/20">Infraestructura</span>
          <span class="text-xs font-semibold text-emerald-400">$397 - $597 USD</span>
        </div>
        <h2 class="font-semibold text-sm text-white mb-1">Inventario Atómico en Vivo</h2>
        <p class="text-xs text-slate-400 mb-3 leading-relaxed">Descuento inmediato ante orders/paid con candado contra sobreventas.</p>
        <div class="text-[11px] text-slate-500 border-t border-slate-800/80 pt-2 flex justify-between">
          <span>Estado:</span>
          <span class="text-emerald-400 font-mono">LISTO LOCAL</span>
        </div>
      </div>
    </div>

    <!-- Consola Interactiva -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-2xl">
      <div class="flex items-center justify-between mb-3">
        <div>
          <h2 class="text-sm font-semibold text-white">Consola de Mando Directo</h2>
          <p class="text-xs text-slate-400">Envía instrucciones al Supervisor Maestro de Tech Sandoval</p>
        </div>
        <span class="text-[11px] font-mono text-sky-400 bg-sky-500/10 px-2 py-0.5 rounded border border-sky-500/20">gemini-3.8-flash</span>
      </div>

      <div id="chat-box" class="bg-slate-950 border border-slate-800/80 rounded-lg p-4 h-64 overflow-y-auto mb-3 space-y-3 font-mono text-xs text-slate-300">
        <div class="text-slate-500">[Sistema]: Panel de control en línea. Los 3 productos están cargados en modo local. Puedes escribir una orden o consulta a continuación.</div>
      </div>

      <div class="flex gap-2">
        <input type="text" id="prompt-input" onkeydown="if(event.key==='Enter')enviarOrden()" placeholder="Escribe una orden para los agentes (ej: Dame el pitch de venta para barberías)..." class="flex-1 bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-sky-500 transition">
        <button onclick="enviarOrden()" class="bg-sky-600 hover:bg-sky-500 text-white font-medium px-4 py-2 rounded-lg text-xs transition">Enviar</button>
      </div>
    </div>
  </div>

  <script>
    async function enviarOrden() {
      const input = document.getElementById('prompt-input');
      const box = document.getElementById('chat-box');
      const prompt = input.value.trim();
      if (!prompt) return;

      box.innerHTML += `<div class="text-sky-300"><strong>Tú:</strong> ${prompt}</div>`;
      input.value = '';
      box.scrollTop = box.scrollHeight;

      try {
        const res = await fetch('/api/orden', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({prompt: prompt})
        });
        const data = await res.json();
        box.innerHTML += `<div class="text-emerald-300"><strong>Supervisor:</strong> ${data.respuesta.replace(/\\n/g, '<br>')}</div>`;
      } catch (err) {
        box.innerHTML += `<div class="text-rose-400"><strong>Error:</strong> No se pudo procesar la solicitud con el supervisor.</div>`;
      }
      box.scrollTop = box.scrollHeight;
    }
  </script>
</body>
</html>
"""

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode("utf-8"))

    def do_POST(self):
        if self.path == "/api/orden":
            length = int(self.headers.get("content-length", 0))
            body = json.loads(self.rfile.read(length))
            user_prompt = body.get("prompt", "")

            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={API_KEY}"
            payload = {
                "contents": [{
                    "parts": [{"text": f"Eres el Supervisor Maestro de Tech Sandoval. Responde con concisión operativa y enfoque B2B a la siguiente orden: {user_prompt}"}]
                }]
            }
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    respuesta = data["candidates"][0]["content"]["parts"][0]["text"]
            except Exception as e:
                respuesta = f"Error al procesar con el modelo: {e}"

            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"respuesta": respuesta}).encode("utf-8"))

print(f"🚀 Panel Tech Sandoval activo en http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    httpd.serve_forever()
