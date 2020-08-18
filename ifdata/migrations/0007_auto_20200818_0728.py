# Generated by Django 3.1 on 2020-08-18 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ifdata', '0006_auto_20200818_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='ifthis',
            name='if_type',
            field=models.ForeignKey(blank=True, help_text='条件类型', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ifdata.ifttttype'),
        ),
        migrations.AlterField(
            model_name='ifthis',
            name='that_action',
            field=models.ManyToManyField(blank=True, help_text='动作行为', to='ifdata.ThatAction'),
        ),
    ]