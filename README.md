# GeoApp
1.install vagrant and virtualbox

2.vagrant up

3.ssh vagrant

4.python manage.py runserver 0.0.0.0:8000

5.go to localhost:8180

6.python manage.py migrate

7.python manage.py collectstatic

#packages
8. cd XlsxWriter
9. sudo python setup.py install

10. cd django-admin-bootstrapped-2.4.0  
11. sudo python setup.py install


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'
# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_ROOT = u'/home/dewalt/REOT/media'
MEDIA_URL = '/media/'
STATIC_ROOT = u'/home/dewalt/REOT/static'
STATIC_URL = '/static/'
