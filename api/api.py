from fastapi import FastAPI, HTTPException
from datetime import datetime
import requests
from typing import Union

app = FastAPI()

@app.get("/yvyryryi/visualize/{init_date}-{final_date}")
async def visualize(init_date: Union[str, datetime], final_date: Union[str, datetime]):
    try:
        if isinstance(init_date, str):
            init_date = datetime.strptime(init_date, '%Y/%m/%d-%H/%M')
        if isinstance(final_date, str):
            final_date = datetime.strptime(final_date, '%Y/%m/%d-%H/%M')
        init_date_str = init_date.strftime("'%Y-%m-%d %H:%M:%S'")
        final_date_str = final_date.strftime("'%Y-%m-%d %H:%M:%S'")
        query = f"SELECT * FROM yvyryryi WHERE __time >= {init_date_str} AND __time < {final_date_str}"
        response = requests.post(
            'http://localhost:8888/druid/v2/sql',
            headers={'Content-Type': 'application/json'},
            json={
                "query": query,
                "context": {"sqlQueryId": "request01"},
                "header": True,
                "typesHeader": True,
                "sqlTypesHeader": True,
            }
        )
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error querying Druid: {str(e)}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
