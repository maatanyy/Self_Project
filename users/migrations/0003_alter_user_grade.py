# Generated by Django 4.0.1 on 2022-02-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_grade_user_influencer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(blank=True, choices=[('1', 'GRADE_1'), ('2', 'GRADE_2'), ('3', 'GRADE_3'), ('4', 'GRADE_4')], max_length=10),
        ),
    ]
