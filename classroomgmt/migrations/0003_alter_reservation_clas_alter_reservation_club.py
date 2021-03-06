# Generated by Django 4.0.4 on 2022-05-26 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroomgmt', '0002_alter_reservation_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='clas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='classroomgmt.clas'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroomgmt.club'),
        ),
    ]
