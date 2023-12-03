from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional
import httpx
import os

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]=True



app=FastAPI()

@app.get('/blog')
def index(limit=10,published:Optional[bool]=True,sort:Optional[str]=None):
    if published:
        return {'data':f'blog list {limit}'}
    else:
        return {'data':'all data'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

@app.post('/blog')
def create_blog(blog:Blog):
    return blog
    return {'data':'Ram'}


# @app.get("/download")
# async def download_from_link(link: str):
#     try:
#         async with httpx.AsyncClient() as client:
#             response = await client.get(link)

#             if response.status_code == 200:
#                 # Assuming you want to return the content of the downloaded file
#                 return {"content": response.text}

#             raise HTTPException(status_code=response.status_code, detail="Failed to download content")

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

@app.get("/download-file")
async def download_and_save_file(link: str, folder_path: str = "downloads", file_name: str = "downloaded_file.txt"):
    try:
        # Ensure the specified folder exists, create it if not
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, file_name)

        async with httpx.AsyncClient() as client:
            response = await client.get(link)

            if response.status_code == 200:
                # Save the content to a file in the specified folder
                with open(file_path, "wb") as file:
                    file.write(response.content)

                return {"message": f"File downloaded and saved as {file_path}"}

            raise HTTPException(status_code=response.status_code, detail="Failed to download file")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))