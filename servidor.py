from codigo import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="Meu app de IA", description="Traduza o texto que você quiser para qualquer língua")

add_routes(app, chain, path="/tradutor")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)