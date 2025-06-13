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

@app.get("/new-endpoint")
def get_version():
    return {"message": "this is my new endpoint.", "extra": "I am testing via CI/CD"}

@app.get("/new-endpoint-one")
def get_version_one():
    return {"message": "this is my new endpoint.", "extra": "I am testing via CI/CD"}


@app.get("/new-endpoint-two")
def get_version_two():
    return {"message": "this is my new endpoint.", "extra": "I am testing via CI/CD"}

@app.get("/new-endpoint-three")
def get_version_three():
    return {"message": "this is my new endpoint.", "extra": "I am testing via CI/CD"}

@app.get("/hello-amit")
def get_version_hello_amit():
    return {"message": "this is my new endpoint.", "extra": "I am testing via CI/CD"}


