import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AI_Digital_Notice_Board.settings')
application = get_asgi_application()
