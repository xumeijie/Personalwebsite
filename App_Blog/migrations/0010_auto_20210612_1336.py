# Generated by Django 3.2.3 on 2021-06-12 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0009_leavemsg_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavemsg',
            name='replay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='replies', to='App_Blog.leavemsg'),
        ),
        migrations.AddField(
            model_name='leavemsg',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rootleave', to='App_Blog.leavemsg'),
        ),
        migrations.AlterField(
            model_name='leavemsg',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parentleave', to='App_Blog.leavemsg'),
        ),
    ]
