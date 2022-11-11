# Playground Final Project
Desarrollamos en dupla Daniel Sancho y Hugo Adrian Toledo una aplicación estilo web blog programada con Python en Django que tendrá admin, perfiles, registro, páginas y formularios

# Instrucciones para ejecutar este proyecto

- Crear Directorio del proyecto

### 1. Abrir Git Bash para `Windows` o una terminal para `Linux/Unix`.

### 2. Crear directorio de trabajo para el proyecto de curso 
```bash
cd
mkdir -p Documents/coder_projects
cd Documents/coder_projects
ls 
```

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/carlosdanielsancho/FinalProject.git

git checkout develop_danielsancho
git checkout develop_adriantoledo
```

### 3. Crear y activar entorno virtual
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```
Se instalarán: 
Django==4.1.2
django-ckeditor==6.5.1
Pillow==9.3.0```

### 5. Navegamos hacia la carpeta del proyecto `our_blog`
```bash
cd our_blog
```

### 6. Se crean las migraciones que son una "plantilla" para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py makemigrations
```

### 7. Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py migrate
```

### 8. Se crea el super usuario para nuestro proyecto de Django, **Solo si no se ha creado**
```bash
python manage.py createsuperuser
```
Ingrese `Username`, `Email address` y `Password` 

### 9. Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/`
```bash
python manage.py runserver
```
