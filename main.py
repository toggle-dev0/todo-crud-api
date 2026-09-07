from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def main():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
def server_health():
    return { "status": "ok" }