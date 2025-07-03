# API Avance - FastAPI

Una API desarrollada con FastAPI para el proyecto Avance.

## Instalación

1. **Crear y activar entorno virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\Activate.ps1  # En Windows PowerShell
   # o
   venv\Scripts\activate.bat   # En Windows CMD
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Ejecutar el servidor de desarrollo

```bash
python run.py
```

O directamente con uvicorn:
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Acceder a la API

- **API:** http://127.0.0.1:8000
- **Documentación interactiva (Swagger):** http://127.0.0.1:8000/docs
- **Documentación alternativa (ReDoc):** http://127.0.0.1:8000/redoc

### Endpoints disponibles

- `GET /` - Mensaje de bienvenida
- `GET /health` - Health check del servicio
- `GET /items/{item_id}` - Ejemplo con parámetros

## Tecnologías utilizadas

- **FastAPI** - Framework web moderno y rápido
- **Uvicorn** - Servidor ASGI de alto rendimiento
- **Pydantic** - Validación de datos
- **Python 3.13** - Lenguaje de programación

## Estructura del proyecto

```
Avance/
├── venv/                 # Entorno virtual
├── app/                  # Módulos de aplicación
├── main.py              # Punto de entrada de FastAPI
├── run.py               # Script para ejecutar servidor
├── requirements.txt     # Dependencias
└── README_FASTAPI.md    # Esta documentación
```
