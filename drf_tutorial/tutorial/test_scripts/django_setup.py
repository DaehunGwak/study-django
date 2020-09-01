import os
import sys
import django
from pathlib import Path

project_path = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(project_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')
django.setup()
