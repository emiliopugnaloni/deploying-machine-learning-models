from fastapi import FastAPI

app = FastAPI() # instantiate the FastAPI app

@app.get("/") # define a GET endpoint in the api
async def root(): # this function will be called when the endpoint is accessed
    return {"message": "Hello World"}

@app.get("/square") # define a GET endpoint in the api. To test: http://localhost:8000/square?num=3 (we passed the with ?)
async def square(num: int): # this function will be called when the endpoint is accessed. We have to specifi a "int" 
    result = num ** 2
    return {"squared": result}

# we can check the doc with: http://localhost:8000/docs
# to run the app, use the command: uvicorn main:app --reload in the terminal
