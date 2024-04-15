from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.put("/")
async def put():
    return {"message": "hello from the put route"}

@app.get("/item")
async def list_items():
    return{"message": "list items route"}

@app.get("/items/foo")  # Define the endpoint /items/foo
async def read_item():
    return {"item_id": "foo"}