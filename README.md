Hackathon-kit
===========

##### SETUP
```
- Install heroku toolbelt (https://toolbelt.heroku.com/)
- Install git
- Install python 2.7.6
- Install pip (e.g. sudo easy_install pip)
```

```
<clone our app to a local git repository>
$ sudo pip install -r requirements.txt
$ heroku apps:create hackathon-demo 
$ git push heroku master
```

##### Migrations
Create new migrations
```
$ python manage.py makemigrations
```

Run migrations
```
$ python manage.py migrate
```

##### Run Server
```
$ python manage.py runserver
```

##### Admin Panel
Create a superuser
```
$ python manage.py createsuperuser
Visit http://127.0.0.1:8000/admin/
```