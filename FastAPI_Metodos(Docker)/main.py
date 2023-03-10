##pip freeze > requirements.txt

##correr la API

##uvicorn main:app --reload

##http://127.0.0.1:8000/docs#


from fastapi import FastAPI, Body, Depends
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 
from sqlalchemy import MetaData

import uvicorn

##crea el archivo todo de la db
Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()


@app.get("/")
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item




@app.post("/")
def addItem(item:schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item




@app.put("/{id}")
def updateItem(id:int, item:schemas.Item, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject


@app.delete("/{id}")
def deleteItem(id:int, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item was deleted...'

if __name__=="__main__":
    uvicorn.run(app,port=8000, host="0.0.0.0")

##para correr, en el html la direccion es "http://127.0.0.1:8000/docs#" y en terminal poner "docker run -p 8000:8000 fastapi-crud"

#Para detener es "docker container ls"
#despues checar el CONTAINER ID... y "docker stop (containerID)"