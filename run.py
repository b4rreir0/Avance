#!/usr/bin/env python3
"""
Script para ejecutar el servidor FastAPI en desarrollo
"""
import uvicorn
from main import app

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True,  # Recarga automática en desarrollo
        log_level="info"
    )
