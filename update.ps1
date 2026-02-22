# update.ps1 - Script de Despliegue Automatizado para Oscar
Write-Host "🇨🇱 Iniciando actualización de agentes..." -ForegroundColor Cyan

# 1. Gestión de respaldos (Solo uno)
if (Test-Path "main_orquestador.py") {
    if (Test-Path "main_orquestador.py.bak") { Remove-Item "main_orquestador.py.bak" -Force }
    Rename-Item "main_orquestador.py" "main_orquestador.py.bak"
    Write-Host "📦 Respaldo anterior creado y basura vieja eliminada." -ForegroundColor Yellow
}

# 2. Descarga de archivos actualizados desde GitHub
$baseUrl = "https://raw.githubusercontent.com/oogazn/agentemasaje/main"

Invoke-WebRequest -Uri "$baseUrl/main_orquestador.py" -OutFile "main_orquestador.py"
Invoke-WebRequest -Uri "$baseUrl/agentes/meta_explorador.py" -OutFile "agentes/meta_explorador.py"
Invoke-WebRequest -Uri "$baseUrl/agentes/clasificador.py" -OutFile "agentes/clasificador.py"

Write-Host "✅ Ecosistema actualizado con éxito. Listo para correr." -ForegroundColor Green
