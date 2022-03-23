# Generated by Django 4.0.3 on 2022-03-23 12:20

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField(blank=True)),
                ('created_on', django_jalali.db.models.jDateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('created_on', django_jalali.db.models.jDateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.CharField(editable=False, max_length=11, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('slug', models.SlugField(editable=False)),
                ('is_valid', models.CharField(choices=[('rejected', 'رد'), ('approved', 'تائید'), ('pending', 'در انتظار')], default='pending', max_length=20, verbose_name='اعتبارسنجی')),
                ('created_on', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='main.tag', verbose_name='تگ ها')),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.CharField(editable=False, max_length=11, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات')),
                ('body', models.TextField(verbose_name='کد')),
                ('lang', models.CharField(choices=[('arduino', 'Arduino'), ('bash', 'Bash'), ('c', 'C'), ('cpp', 'C++'), ('csharp', 'C#'), ('css', 'CSS'), ('dart', 'Dart'), ('docker', 'DockerFile'), ('docker-compose', 'DockerCompose'), ('go', 'Go'), ('html', 'HTML'), ('java', 'Java'), ('js', 'JavaScript'), ('json', 'JSON'), ('lua', 'Lua'), ('md', 'markdown'), ('mysql', 'MySQL'), ('php', 'PHP'), ('python', 'Python'), ('rb', 'Ruby')], max_length=250, verbose_name='زبان برنامه\u200cنویسی')),
                ('created_on', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=250, verbose_name='نظر')),
                ('created_on', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ticket')),
            ],
        ),
        migrations.AddIndex(
            model_name='snippet',
            index=models.Index(fields=['id'], name='main_snippe_id_9d06f9_idx'),
        ),
    ]
