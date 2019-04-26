import os
import threading
import time

from invoke import task, run


def wait_port_is_open(host, port):
    import socket
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            sock.close()
            if result == 0:
                return
        except socket.gaierror:
            pass
        time.sleep(1)

@task
def init_db(ctx, recreate_db=False):
    wait_port_is_open(os.getenv('DB_HOST', 'db'), 5432)
    ctx.run('python code_solutions/manage.py makemigrations')
    ctx.run('python code_solutions/manage.py migrate')

@task
def run(ctx):
    init_db(ctx, recreate_db=False)

    # ctx.run('uwsgi --ini uwsgi.ini')
    ctx.run('python code_solutions/manage.py runserver 0.0.0.0:8990')
