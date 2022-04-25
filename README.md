# Proyecto para pedir préstamo

## Instalación
Descargar el repositorio con:

```
git clone https://github.com/fedemarkco/proyectoMoniOnline.git
```
El proyecto se encuentra en un contenedor Docker, para poder levantarlo, se tiene que ejecutar:

```
cd proyectoMoniOnline
docker-compose up
```
El contenedor fue configurado para que ejecute
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```
También he puesto que cree un superusuario con los siguientes datos:
<br>Username: Marco
<br>Password: 1234
<br>Email: fedemarkco@gmail.com
 
Estos datos serán utilizados por el sitio de administración del proyecto.

Para acceder al formulario de pedido del préstamo, se tiene que ingresar a la URL
```
 http://127.0.0.1:8000
```
Y para acceder al sitio de administración, se tiene que ingresar a la URL
```
http://127.0.0.1:8000/loginView/
```
El usuario que se va a poder loguear, es el creado anteriormente (creado para ser utilizado en este proyecto), es decir el usuario Marco con contraseña 1234.

Nota: Para la verificación del estilo del código he utilizado pycodestyle.
