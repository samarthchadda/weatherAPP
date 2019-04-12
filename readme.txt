1.      create new project , in cmd,
	django-admin startproject weatherapp

2. 	create new app , in cmd ,
	python manage.py startapp weath

3. 	add app to the project (in settings.py), 	
	add 'weath'  in INSTALLED_APPS

4. 	Then do migrations 
	python manage.py migrate 

5.   	create superuser,
	python manage.py createsuperuser

6.   	add template into the project

7. 	call the APIs,  using api keys etc

8. 	install the requests
	pip install requests

9.	after doing  ,  
	r=requests.get(url.format(city))
	print(r.text)

	extract necessary data from the cmd, and create a dictionary

10.  	create table in database , to store a bunch of cities

11. 	then makemigrations etc in cmd

12. 	add the same( register )  in admin.py

13.  	add cities through admin dashboard
	 http://127.0.0.1:8000/admin

14. 	also make loop to display all cities

15. 	Enable the submit button , create forms.py
