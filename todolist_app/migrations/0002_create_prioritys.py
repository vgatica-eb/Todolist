from django.db import migrations
from todolist_app.models import Priority


def create_priorities(*args):
    Priority.objects.bulk_create([
        Priority(description='low', order=0),
        Priority(description='medium', order=1),
        Priority(description='high', order=2),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('todolist_app', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_priorities),
    ]
