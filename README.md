# csv_merge_and_reader

[![python3.8](https://img.shields.io/badge/python-3.8-blue.svg)]()

## Documentation

#### Add INSTALLED_APPS setting:
```
INSTALLED_APPS = [
    'datatable.apps.DatatableConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'django_tables2',
    'django_filters',
]
```

#### How to run it
```
git clone https://github.com/polifa/csv_merge_and_reader.git
or
download as ZIP and extract
```

```
cd into the folder
pip install -r requirements.txt
connect your database and edit settings.py <https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-DATABASES>
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Access the web page though this link: http://127.0.0.1:8000/datatable

There are two csv files inside the datatable/static with the correct headers

## Site Admin installation

**Admin Account**  
```
python manage.py createsuperuser

There's a default admin user
user: admin
password: admin

Can also manage user accounts through admin page
```
Access the web page through this link: http://127.0.0.1:8000/admin

## License

This software is licensed under the BSD 3-Clause License. For more information, read the file `LICENSE`.
