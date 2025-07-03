# Punto de entrada principal para FastAPI
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Crear la aplicación FastAPI
app = FastAPI(
    title="API Avance",
    description="Una API desarrollada con FastAPI",
    version="1.0.0"
)

# Ruta básica de prueba
@app.get("/")
async def read_root():
    return {"message": "¡Hola! API funcionando correctamente", "status": "success"}

# Ruta de health check
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "API Avance"}

# Ruta de ejemplo con parámetros
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
