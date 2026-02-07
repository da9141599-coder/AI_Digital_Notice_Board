import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AI_Digital_Notice_Board.settings')
application = get_wsgi_application()
