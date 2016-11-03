"""
WSGI config for closetProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
import site

#from django.core.wsgi import get_wsgi_application

site.addsitedir('/opt/closet2/local/lib/python3.5/site-packages')

sys.path.append('/home/ballsuser/closetProject')
sys.path.append('/home/ballsuser/closetProject/closetProject')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "closetProject.settings")

activate_env=os.path.expanduser("/opt/closet2/bin/activate_this.py")

exec(open(activate_env).read(), dict(__file__=activate_env))
#execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
