"""
WSGI config for RecipeManagement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
project_home = '/home/peterkiwanda/RecipeManagement_API_Project/BE_Capstone_Project/RecipeManagement'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path



from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RecipeManagement.settings')

application = get_wsgi_application()
