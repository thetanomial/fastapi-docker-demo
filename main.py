from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World", "version": "2.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "fastapi-demo"}

@app.get("/version")
def get_version():
    return {"version": "2.0", "deployed_via": "github_actions"}