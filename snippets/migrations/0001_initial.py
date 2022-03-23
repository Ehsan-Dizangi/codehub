# Generated by Django 4.0.3 on 2022-03-23 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
        migrations.AddIndex(
            model_name='snippet',
            index=models.Index(fields=['id'], name='snippets_sn_id_828944_idx'),
        ),
    ]