#!/bin/bash
echo "Levantando Hub Visual del Laboratorio S-Prime en el Puerto 8060..."
cd ~/sprime_cloud_core/laboratorio_software
python3 -m http.server 8060 &
npm exec localtunnel --port 8060 --subdomain sprime-arsenal &
echo "El Arsenal Visual está en vivo en: https://sprime-arsenal.loca.lt"
