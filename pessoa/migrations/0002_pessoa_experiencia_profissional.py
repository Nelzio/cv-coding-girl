# Generated by Django 4.2.7 on 2023-11-20 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='experiencia_profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoa.experienciaprofissional'),
        ),
    ]