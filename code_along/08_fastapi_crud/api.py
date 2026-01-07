from fastapi import FastAPI

app = FastAPI()
@app.get("/books")
async def read_books():
    return{"books": "Hello Api books"}
