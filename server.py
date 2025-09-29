from math import ceil, sqrt
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "API is running!"}

@app.get("/close_int_squares/{number}")
def get_close_squares(number: int, q: Optional[str] = None):
    # We gonna use sqrt to get current root
    
    root = sqrt(number)
    # Get right and left closest integer
    right_int = ceil(root)
    left_int = int(root)

 
    # ceil and int can be the same only if the initial number for the is int
    if right_int == left_int:
        left_int_square = (left_int - 1) ** 2
        right_int_square = (right_int + 1) ** 2

    else:
        left_int_square = left_int ** 2
        right_int_square = right_int ** 2

    # Root can't be below 0 and that's mean that we cannon get left value lower than zero
    if left_int == 0:
        left_int_square = None


    return {"left_int_squre": left_int_square, "right_int_square": right_int_square}
