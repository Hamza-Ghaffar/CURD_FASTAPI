# main.py (keep CORS middleware setup)

import uvicorn
import db_models
from fastapi import FastAPI
from database import db_engine
from routes import main_router
from auth import Login_route
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()

origins = [
    "http://127.0.0.1:5500",
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify specific origins instead of "*"
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # You can adjust these methods as needed
    allow_headers=["*"],  # You can specify specific headers if necessary
)

app.include_router(main_router)
app.include_router(Login_route)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8888)

# create tables in databae
db_models.Base.metadata.create_all(bind=db_engine)
