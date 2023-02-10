#especificar imagen
FROM python:3.10

#organizar carpetas DEL container en workdir
WORKDIR /fast-api


##hacer pip freeze > requirements.txt

##se copian los requirements hechos (uvicorn, fast api, sqlalchemy etc)
COPY requirements.txt .

##hay que instalar todos los requirements 

RUN pip install -r requirements.txt 

#se copia la carpeta "app" y su nombre igual "app"

COPY / /

#se especifica el entry point del contenedor 
CMD [ "python" , "/main.py"]

# se tuvo que crear imagen  docker build -t fastapi-crud .

##para correr, en el html la direccion es "http://127.0.0.1:8000/docs#" y en terminal poner:
#"docker run -p 8000:8000 fastapi-crud"


# Para detener el container puede ser con CTRL+C, algunas veces no funciona entonces se puede ejecutar
# lo siguiente::

    # Se debe saber que ID tiene el container con:
    #     docker container ls

    # para detener el conteiner se ejecuta lo siguiente:
    #     docker stop containerID



