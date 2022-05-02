# Generated by Django 4.0.4 on 2022-05-02 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_doc_docfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doclist', to=settings.AUTH_USER_MODEL),
        ),
    ]