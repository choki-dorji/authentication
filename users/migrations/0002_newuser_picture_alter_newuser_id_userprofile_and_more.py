# Generated by Django 4.0 on 2022-01-11 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='profiel_pics')),
                ('dob', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='users.newuser')),
            ],
        ),
        migrations.CreateModel(
            name='Fileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='photo_directory_path')),
                ('dob', models.DateTimeField()),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='users.newuser')),
            ],
        ),
    ]
