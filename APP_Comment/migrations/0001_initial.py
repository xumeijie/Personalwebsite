# Generated by Django 3.2.6 on 2021-10-25 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
                ('browserId', models.CharField(max_length=24, null=True)),
                ('articleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Blog.article')),
                ('parentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentComment', to='APP_Comment.comment')),
                ('replayTo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL)),
                ('root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rootComment', to='APP_Comment.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '评论',
                'db_table': 'comment',
                'ordering': ['-time'],
            },
        ),
    ]
