# Generated by Django 4.0.2 on 2022-12-09 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_aluno_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='observacao',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='qualProblema',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
