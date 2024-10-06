from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

@app.get("/yvyryryi/download/{init_date}-{final_date}", response_model=...)
async def download(init_date: str, final_date: str):
    ### make the query towards the apache druid endpoint
    ### create fits files
    ### compress fits files
    ### send

@app.get("/yvyryryi/visualize/{init_date}-{final_date}", response_model=List[Item])
async def visualize(init_date: str, final_date: str):
    item = requests.get(
        'http://localhost:8888/druid/v2/sql',
        headers = {'Content-Type' : 'application/json'},
        data = {
            "query": f"SELECT * FROM yvyryryi WHERE {init_date} < date < {final_date}",
            "context" : {"sqlQueryId" : "request01"},
            "header" : True,
            "typesHeader" : True,
            "sqlTypesHeader" : True,
        }
    )
    ## {rel_time: ..., velocity: ...}
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
