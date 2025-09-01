from fastapi import FastAPI

app = FastAPI()

# We then use app as a decorator
@app.get('/welcome')
def welcome():
    return {
        'message' : 'Hello world !!!!'
    }
