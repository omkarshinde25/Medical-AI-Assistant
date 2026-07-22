from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware

app=FastAPI(title="Medical Assistant API", description="API for AI Medical Assitance Chatbot")

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_header=["*"]
)

# middleware exception handlers
app.middleware("http")(catch_exception_middleware)

# Routers

# 1: Upload PDFs documents
# 2: Asking query









