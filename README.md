# securitec music

## crear y activar entorno virtual
```
 python3 -m venv env
 source env/bin/activate
```

## instalar dependencias
```
 pip install -r requirements.txt
```

## crear y ejecutar migraciones
```
 python manage.py makemigrations
 python manage.py migrate 
```

## crear superusuario
```
 python manage.py createsuperuser --email admin@securitec.com --username admin
```

## ejecutar servidor
```
 python manage.py runserver localhost:8080
```
