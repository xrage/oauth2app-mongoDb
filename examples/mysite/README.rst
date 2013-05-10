The example site uses django-mongodb-engine. ::
    
    git clone git@github.com:dkvermavit/oauth2app-mongoDb.git oauth2app-mongoDb
    cd oauth2app-mongoDb/examples/mysite
    git checkout master
    pip install https://github.com/dkvermavit/oauth2app-mongoDb/tarball/master https://github.com/django-nonrel/django-nonrel/tree/django-1.3.2 django-uni-form djangotoolbox django-mongodb-engine
    python manage.py syncdb --noinput
    python manage.py runserver

Visit http://127.0.0.1:8000/ on your local machine and follow the instructions.
