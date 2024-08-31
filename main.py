from fastapi import FastAPI
from src.routes import auth_routes

app = FastAPI()

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Twitter clone API"}

# Include authentication routes
app.include_router(auth_routes.router, prefix="/auth")
