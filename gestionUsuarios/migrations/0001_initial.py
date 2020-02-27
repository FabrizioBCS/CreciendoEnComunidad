# Generated by Django 3.0.2 on 2020-02-27 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionActividades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferencias_valor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField()),
                ('id_valor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionActividades.Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Preferencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField()),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionActividades.Categoria')),
                ('id_distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionActividades.Distrito')),
            ],
        ),
    ]