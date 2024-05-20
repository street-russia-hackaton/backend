# Generated by Django 5.0.6 on 2024-05-20 19:14

import datetime

import core.constants
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_userpassport_passport_issued_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userpassport",
            name="passport_issued_at",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Дата выдачи"
            ),
        ),
        migrations.AlterField(
            model_name="userpassport",
            name="passport_number",
            field=models.CharField(
                default="",
                max_length=core.constants.UserFieldsLength["MAX_LENGTH_NUMBER"],
                validators=[
                    django.core.validators.RegexValidator(
                        "^\\d{1,20}$", message="Only digits are allowed"
                    )
                ],
                verbose_name="Номер паспорта",
            ),
        ),
        migrations.AlterField(
            model_name="userpassport",
            name="passport_series",
            field=models.CharField(
                default="",
                max_length=core.constants.UserFieldsLength["MAX_LENGTH_SERIES"],
                validators=[
                    django.core.validators.RegexValidator(
                        "^\\d{1,10}$", message="Only digits are allowed"
                    )
                ],
                verbose_name="Серия паспорта",
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="phone",
            field=models.CharField(
                max_length=core.constants.UserFieldsLength["MAX_LENGTH_PHONE"],
                unique=True,
                verbose_name="Телефон",
            ),
        ),
    ]