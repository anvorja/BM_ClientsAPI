

# BM_Clients readme

Como aún no está dockerizado hacemos lo siguiente:

Creamos el entorno virtual y lo activamos

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalamos dependencias

```bash
pip install -r requirements.txt
```

Con pgadmin ya debemos haber creado la base de datos clientes_db

Ahora, configurar las credenciales de postgres en el settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'clientes_db1',
        'USER': 'postgres',
        'PASSWORD': 'la que usa en tu sistema',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Hacemos migraciones



```python
python3 manage.py makemigrations
python3 manage.py migrate
```

Run server (pueden correr en el puerto que deseen por ahora. Usaré el 7676)

```python
python3 manage.py runserver 7676
```

Pueden crear el superusuario para agregar  los clientes o pueden hacerlo desde la interfaz que se proporciona en http://127.0.0.1:7676/

```python
python3 manage.py createsuperuser
```

Una vez registrados algunos clientes puedes usar el html que está en la carpeta prueba para ver que consume unos datos de clientes registrados
