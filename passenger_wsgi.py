import sys, os

INTERP = os.path.join(os.environ['HOME'], '', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
cwd = os.getcwd()
sys.path.append(os.getcwd())

# INTERP = "/home/lemonaid/dj/bin/python3" # absolute path to your virtual env
# #INTERP is present twice so that the new python interpreter
# #knows the actual executable path
# if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
# cwd = os.getcwd()
# sys.path.append(cwd)
sys.path.append(cwd + '/helloworld')  # name of your Django project
sys.path.insert(0,cwd+'../venv/bin') # virtual env # relative path to your virtual env
sys.path.insert(0,cwd+'../venv/lib/python3.8/site-packages') # relative path to your virtual env
os.environ['DJANGO_SETTINGS_MODULE'] = "helloworld.settings" # name of your Django project

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

