from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/blog")
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {"data": f"{limit} published blog from the db"}
    else:
        return {"data": f"{limit} blog from the db"}


@app.get("/blog/unpublished")
def unpublished():
    return{"data":"all unpublished blogs"}

@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")  
def comments(id,limit =10):
    return limit
    return {"data": {"1","2"}}


class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post("/blog")
def create_blog(blog :Blog):
    
    return {"data": f"blog is created title as { blog.title}"}

import uvicorn
if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port = 9000)





