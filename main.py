from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic
from mylib.logic import phrases

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}

@app.get("/search/{value}")
async def search(value: str):
    """Pages to search in wikipedia"""

    result = search_wiki(value)
    return {"results": result}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""

    result = wikilogic(name)
    return {"results": result}

@app.get("/phrases/{phrase}")
async def phrases(phrase: str):
    """Retrieve wikipedia page and return phrases"""

    result = phrases(phrase)
    return {"results": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')