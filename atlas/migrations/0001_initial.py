# Generated by Django 2.0.7 on 2018-08-09 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=60)),
                ('avatar', models.ImageField(upload_to='ProfilePicture/')),
                ('contact_info', models.CharField(max_length=50)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usname', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]