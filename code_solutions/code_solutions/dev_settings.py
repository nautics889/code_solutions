#Database settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'code_solutions',
        'USER': 'code_solutions',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '5432',
    }
}
