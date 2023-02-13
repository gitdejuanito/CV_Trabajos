#especificas imagen
FROM python:3.10   

#organizar las carpetas en workdir
WORKDIR /fast

##se copian los requirements
COPY requirements.txt .

#se instalan los requirements
RUN pip install -r requirements.txt

#se copia la carpeta "app" y su nombre igual "app"
COPY ./app ./app

#se especifica el entry point del contenedor 
CMD [ "python" , "./app/main.py"]


###despues se crea la imagen llamada python_fastapi_helloworld con "docker build -t python_fastapi_helloworld . 

##correr con "docker run python_fastapi_helloworld"








