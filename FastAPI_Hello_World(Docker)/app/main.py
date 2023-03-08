##http://127.0.0.1:8000/docs#

##pip freeze > requirements.txt

from typing import Union

from fastapi import FastAPI
import uvicorn 

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__=="__main__":
    uvicorn.run(app,port=8000, host="0.0.0.0")

    ## es necesario especificar el port y host de la app

##para correr, en el html la direccion es "http://localhost:8000/docs" y en terminal poner "docker run -p 8000:8000 python_fastapi_helloworld"



#Para detener es "docker container ls"
#despues checar el CONTAINER ID... y "docker stop containerID"