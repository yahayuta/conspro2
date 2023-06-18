# conspro2

here is sample of django app development environment for docker using mysql.  
and compete that tutorials  
https://docs.djangoproject.com/en/4.1/intro/tutorial01/  

# start containers

```sh
docker-compose build
docker-compose up -d

CONTAINER ID   IMAGE                     COMMAND                   CREATED          STATUS          PORTS                               NAMES
9cc10ee1bff8   conspro2-web              "python3 manage.py r…"   54 seconds ago   Up 40 seconds   0.0.0.0:8000->8000/tcp              conspro2
633823b5f491   steveltn/https-portal:1   "/init"                   56 seconds ago   Up 44 seconds   80/tcp, 0.0.0.0:3443->443/tcp       conspro2-https-1
c2201c5ec28a   mysql:8                   "docker-entrypoint.s…"   58 seconds ago   Up 48 seconds   0.0.0.0:3306->3306/tcp, 33060/tcp   conspro2-db-1
```

# make init config

```sh
docker exec -it conspro2-web bash

root@b50f2861bc6e:/django# python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  
  root@b50f2861bc6e:/django# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@admin.com
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
root@b50f2861bc6e:/django# python manage.py startapp sample
root@b50f2861bc6e:/django#
```

# endpoints
https://localhost:3443/admin/  
https://localhost:3443/conspro2/  

# troubleshoot

if see this on docker logs
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "/usr/local/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.10/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check_migrations()
  File "/usr/local/lib/python3.10/site-packages/django/core/management/base.py", line 486, in check_migrations
    executor = MigrationExecutor(connections[DEFAULT_DB_ALIAS])
  File "/usr/local/lib/python3.10/site-packages/django/db/migrations/executor.py", line 18, in __init__
    self.loader = MigrationLoader(self.connection)
  File "/usr/local/lib/python3.10/site-packages/django/db/migrations/loader.py", line 53, in __init__
    self.build_graph()
  File "/usr/local/lib/python3.10/site-packages/django/db/migrations/loader.py", line 220, in build_graph
    self.applied_migrations = recorder.applied_migrations()
  File "/usr/local/lib/python3.10/site-packages/django/db/migrations/recorder.py", line 77, in applied_migrations
    if self.has_table():
  File "/usr/local/lib/python3.10/site-packages/django/db/migrations/recorder.py", line 55, in has_table
    with self.connection.cursor() as cursor:
  File "/usr/local/lib/python3.10/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/django/db/backends/base/base.py", line 259, in cursor
    return self._cursor()
  File "/usr/local/lib/python3.10/site-packages/django/db/backends/base/base.py", line 235, in _cursor
    self.ensure_connection()
  File "/usr/local/lib/python3.10/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/django/db/backends/base/base.py", line 218, in ensure_connection
    with self.wrap_database_errors:
  File "/usr/local/lib/python3.10/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/usr/local/lib/python3.10/site-packages/django/db/backends/base/base.py", line 219, in ensure_connection
    self.connect()
  File "/usr/local/lib/python3.10/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/django/db/backends/base/base.py", line 200, in connect
    self.connection = self.get_new_connection(conn_params)
  File "/usr/local/lib/python3.10/site-packages/django/utils/asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/django/db/backends/mysql/base.py", line 234, in get_new_connection
    connection = Database.connect(**conn_params)
  File "/usr/local/lib/python3.10/site-packages/MySQLdb/__init__.py", line 123, in Connect
    return Connection(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/MySQLdb/connections.py", line 185, in __init__
    super().__init__(*args, **kwargs2)
django.db.utils.OperationalError: (2002, "Can't connect to MySQL server on 'db' (115)")
```
try this
```
docker-compose restart web
```

if see this on docker logs, ok to open
```
Django version 3.2, using settings 'djangopj.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```
