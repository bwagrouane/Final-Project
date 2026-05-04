import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .routers import items, statistics, orders, cart, payments
from .models import model_loader
from .dependencies.config import conf


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(statistics.router, prefix="/statistics", tags=["Statistics"])
app.include_router(cart.router, prefix="/carts", tags=["Carts"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])

model_loader.index()
indexRoute.load_routes(app)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)

    