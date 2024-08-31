from fastapi import FastAPI
from src.database.database import engine, Base
from src.routes import auth_routes, post_routes, user_routes

# Create the tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(post_routes.router, prefix="/post")
app.include_router(user_routes.router, prefix="/user")
