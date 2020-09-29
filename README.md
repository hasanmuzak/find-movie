# find-movie
Find-Movie is a sample project for using &amp; understanding API and front-end technologies.  

Frontend Live : [Front-end live link](https://find-movie-frontend.herokuapp.com/#/)  
Backend Live : [Backend-end live link](https://find-movie-api.herokuapp.com/)  

---
API URLS EXAMPLE
1. https://find-movie-api.herokuapp.com/api/movies-series/all
2. https://find-movie-api.herokuapp.com/api/movies-series/detail/<slug>
3. https://find-movie-api.herokuapp.com/api/movies-series/links/<slug>
4. Other urls can be found in backend/*urls.py files.  

### Technologies used

**Backend :** Python - Django/Django REST  
**Frontend :** Vue.js - Tailwindcss
### Usage
---
**Backend Installation**
- Create a virtual environment in "backend" folder. Type the code below in terminal :  
```python -m venv env```
- You need to activate the virtual environment that you've created. Type the code below in terminal :  
```source venv/bin/activate```
- Install the required packages. (Read ***backend/requirements.txt***) (via ```pip install <required-package>```)
- After installing required packages, its done. Run :   
```python manage.py runserver```
---
**Frontend Installation**
- Go "frontend" directory from terminal and run the code below in terminal :  
```npm install```
- It will install the required modules. After it installed successfuly type the code below in terminal :  
```npm run serve```
- You are done!
## Important!
1. You need to migrate db and create a superuser in backend via ```python manage.py makemigrations``` and then ```python manage.py migrate``` and then ```python manage.py createsuperuser```.
2. Even though you create movie or url in database, it won't work. Because in "frontend/src/store" directory, ***store.js*** file uses custom URL. You need to configure those urls.
