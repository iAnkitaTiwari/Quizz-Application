# Generated by Django 3.0.5 on 2021-05-07 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_question_complaxity'),
    ]

    operations = [
        migrations.CreateModel(
            name='complexity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complexity', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='complaxity',
            field=models.CharField(max_length=100),
        ),
    ]
