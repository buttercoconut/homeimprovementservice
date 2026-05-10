# main.py
from fastapi import FastAPI
from .api import quote_request, contractor

app = FastAPI(title="Home Improvement Service API")

app.include_router(quote_request.router)
app.include_router(contractor.router)
