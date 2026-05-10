# main.py
from fastapi import FastAPI
from .api import user, quote_request, contractor, quote

app = FastAPI(title="Home Improvement Service API")

app.include_router(user.router)
app.include_router(quote_request.router)
app.include_router(contractor.router)
app.include_router(quote.router)

@app.get("/", tags=["healthcheck"])
async def read_root():
    return {"message": "Home Improvement Service API is running."}
