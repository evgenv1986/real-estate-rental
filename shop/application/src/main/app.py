from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.meetRoutes import router

# Создаем экземпляр FastAPI приложения
app = FastAPI(
    title="Real Estate Rental API",
    description="API for real estate rental management system",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене замените на конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутер
app.include_router(router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to Real Estate Rental API"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "real-estate-rental"}

@app.get("/api/v1/info")
async def api_info():
    """API information endpoint"""
    return {
        "version": "1.0.0",
        "name": "Real Estate Rental API",
        "description": "Management system for rental properties"
    }

