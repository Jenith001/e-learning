# Generated by Django 4.1.4 on 2023-08-05 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("devedu", "0017_alter_course_created_on_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewcoursemiddle",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="devedu.course",
            ),
        ),
    ]