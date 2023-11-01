# Usa una imagen base de Python
FROM python:3.9

# Configura el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Instala las dependencias de tu proyecto (si tienes un archivo requirements.txt)
RUN pip install -r requirements.txt

# Ejecuta las migraciones de Django
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expone el puerto 8000 (ajusta según tu configuración)
EXPOSE 8989

# Inicia tu aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8989"]
