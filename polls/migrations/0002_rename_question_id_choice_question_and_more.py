# Generated by Django 4.2 on 2023-05-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="choice",
            old_name="question_id",
            new_name="question",
        ),
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(verbose_name="생성일시"),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.CharField(max_length=200, verbose_name="질문"),
        ),
    ]
