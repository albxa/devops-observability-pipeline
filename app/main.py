from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest

app = FastAPI()

# Prometheus counter
request_count = Counter("request_count", "Number of requests received")

@app.middleware("http")
async def count_requests(request, call_next):
    request_count.inc()
    response = await call_next(request)
    return response

@app.get("/")
def root():
    return {"message": "FastAPI app is running"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
