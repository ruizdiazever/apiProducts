# Tutorial de desarrollo

## Documentacion
- **[Django](https://docs.djangoproject.com/en/3.0/)**
- **[Django Rest Framework](https://www.django-rest-framework.org/)**

## Primeros pasos
-   **Instalar virtualenv**
```bash
$ virtualenv django-vue     # Crear entorno virtual
$ cd django-vue/Scripts     # Ir a la ruta
$ activate                  # Activar entorno virtual
$ pip install django        # Instalar Django
```

-   **Instalar Django, con entorno activado**
```bash
$ pip install django        # Instalar Django en su ultima version
```

-   **Crear proyecto**
```bash
$ django-admin startproject djangovue     # Crear proyecto
$ cd products                             # Ingresamos al proyecto
$ python manage.py runserver              # Ejecutamos el servidor y vemos nuestra pagina de bienvenida
```

- **Crear app api**
```bash
$ python manage.py startapp api
```

- **Registramos dicha app al ```setting.py```**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api', # ACA
]
```

- **Trabajamos en el ```models.py``` de nuestra app ```api```**
```python
from django.db import models

class Producto(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField()
    description = models.TextField(help_text="Descripcion del producto")
    stock = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
```

- **Ejecutamos nuestras migraciones**
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- **Creando productos con el shell de python**
```bash
$ python manage.py shell
```
```shell
>>> from products.models. import Producto
>>> producto_1 = Producto(title='Fideos', description='Fideos a base de huevo.')
>>> product_1.save()
>>> quit()
```

## RESTful APIs
- **Instalamos ```djangorestframework```**
```bash
$ pip install djangorestframework
```

- **Registrar la libreria en nuestro ```settings.py```**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book',
    'rest_framework' # ACA
]
```

- **Crear archivos en nuestra app ```book```**
## SERIALIZER
Nos permitira serializar nuestro modelo, para que pueda ser trasnportado a traves del protocolo HTTP.  
La clase nos permitira transportar nuestros objetos a traves de la red ya sea en un formato json, xml u otro.  
**Ruta de archivo:**

```
products/
        api/  
            serializer.py
```

**Codigo de archivo:**
```python
from .models import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):

    # Con que modelo y campos vamos a trabajar.
    class Meta:
        models = Producto
        fields = ['name', 'stock']
```

## VIEWSETS
Es a traves de este archivos que nosotros vamos a poder hacer un CRUD sobre nuestro objeto, podremos crear, actualizar, consultar y eliminar.  
**CRUD:** Create, Read, Update y Delete.  
**Ruta de archivo:**
```
djangovue/
        book/  
            serializer.py
            viewsets.py
```

**Codigo de archivo:**
```python
from rest_framework import viewsets

from .models import Book
from .serializer import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class =  BookSerializer
```


URLS:
Esta clase va a definir la ruta para nuestro modelo. La ruta GET, POST, PUT, DELETE, entre otras.  
**Ruta de archivo:**
```
djangovue/
        book/  
            serializer.py
            viewsets.py
            urls.py
```

**Codigo de archivo:**
```python
from rest_framework import routers
from .viewsets import BookViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls
```

**Configuraciones:**  
Vamos a nuestro archivo ```urls.py``` de nuestro proyecto e importamos ```include``` de esta manera:
```python
from django.contrib import admin
from django.urls import path, include # ACA

urlpatterns = [
    path('admin/', admin.site.urls),

    # Es muy buena practica incluir una version para nuestra API
    path('api/v1.0/', include('book.urls')), # ACA
]

```  

**Prueba**  
Vamos a nuestra url, [ejemplo](http://127.0.0.1:8000/api/v1.0/books/).
