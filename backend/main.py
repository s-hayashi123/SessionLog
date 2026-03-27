from fastapi import FastAPI
from mangum import Mangum

from routers import members, trainers

app = FastAPI(redirect_slashes=False)
handler = Mangum(app)

app.include_router(members.router)
app.include_router(trainers.router)


@app.get("/health")
def healthcheck():
    return {"status": "OK"}
