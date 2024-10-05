from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    date: str
    v: float
    ### ...

@app.get("/yvyryryi/download/{init_date}-{final_date}", response_model=...)
async def download(init_date: str, final_date: str):
    ### make the query towards the apache druid endpoint
    ### create fits files
    ### compress fits files
    ### send

@app.get("/yvyryryi/visualize/{init_date}-{final_date}", response_model=List[Item])
async def visualize(init_date: str, final_date: str):
    item = ...
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
