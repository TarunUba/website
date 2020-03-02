# Generated by Django 2.2.6 on 2020-02-24 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200225_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='merchant',
            field=models.ForeignKey(limit_choices_to={'groups': 1}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]