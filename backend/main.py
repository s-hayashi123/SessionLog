from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from routers import members, sessions

app = FastAPI(redirect_slashes=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://main.d2dd04fkvprk4q.amplifyapp.com",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)

app.include_router(members.router)
app.include_router(sessions.router)


@app.get("/health")
def healthcheck():
    return {"status": "OK"}
