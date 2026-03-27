from fastapi import FastAPI
from routers import  upload_router, productivity_router,quiz_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="ChatInsight AI")
# Allow CORS
origins = [
    "http://localhost:3000",  # your frontend origin
    "http://127.0.0.1:3000",
    # you can add your production URL later
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allowed origins
    allow_credentials=True,
    allow_methods=["*"],         # allow all HTTP methods
    allow_headers=["*"],         # allow all headers
)
app.include_router(upload_router.router, tags=["Upload Data"])
app.include_router(productivity_router.router, tags=[" AI Productivity Analysis"])
app.include_router(quiz_router.router, prefix="/ai")