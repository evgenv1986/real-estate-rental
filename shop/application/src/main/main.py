#!/usr/bin/env python3
"""
Main entry point for the FastAPI application.
This file serves as the launcher for the application.
"""

import uvicorn
import os
import sys
from pathlib import Path

# Добавляем путь к модулям проекта
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))


class IndexEndpoint:
    def execute(self):pass


class ApplicationConfiguration:
    indexController = IndexEndpoint()


def main():
    """Main function to run the FastAPI application"""

    # Настройки сервера
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    reload = os.getenv("RELOAD", "true").lower() == "true"

    print("🚀 Starting FastAPI application...")
    print(f"📍 Host: {host}")
    print(f"🔗 Port: {port}")
    print(f"🔄 Reload: {reload}")
    print("──────────────────────────────────────")

    app_config = ApplicationConfiguration()

    # Запускаем сервер
    uvicorn.run(
        app="app:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )


if __name__ == "__main__":
    main()