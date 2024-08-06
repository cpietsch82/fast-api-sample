from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import todos, users

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

app.include_router(users.router)
app.include_router(todos.router)
app.include_router(
  admin.router,
  prefix="/admin",
  tags=["admin"],
  dependencies=[Depends(get_token_header)],
  responses={418: {"description": "I'm a teapot"}},
)

@app.get("/")
async def root():
  return {"message": "Hello Bigger Applications!"}