import os
import sys

from django.core.wsgi import get_wsgi_application

# Tambahkan root project ke path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

app = get_wsgi_application()
