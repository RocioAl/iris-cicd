# Práctica 8 — CI/CD con GitHub Actions y GHCR (Dataset Iris)

Proyecto completo listo para ejecutar pruebas con `pytest`, validar integración continua en GitHub Actions y publicar automáticamente la imagen Docker en GitHub Container Registry (GHCR).

## 1. Ejecutar pruebas localmente (CMD de Windows)
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m pytest -v
```

## 2. Subir a GitHub (Actividad 3)
Crea un repositorio vacío en GitHub (por ejemplo `iris-cicd`) sin README ni `.gitignore`, y ejecuta:
```cmd
git init -b main
git add .
git commit -m "Proyecto inicial CI CD"
git remote add origin https://github.com/TU_USUARIO/iris-cicd.git
git push -u origin main
```

## 3. Descargar y ejecutar la imagen publicada en GHCR (Actividad 8)
```cmd
docker pull ghcr.io/tu_usuario/iris-cicd:latest
docker run -d --name iris-cicd -p 8000:8000 ghcr.io/tu_usuario/iris-cicd:latest
```
Abre en el navegador:
- Interfaz HTML: http://localhost:8000/
- Swagger UI: http://localhost:8000/docs
- Salud: http://localhost:8000/health
