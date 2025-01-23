from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.utils.datetime_safe import datetime


class User(models.Model):
    first_name = models.CharField(
        max_length=255,
        validators=[
            MinLengthValidator(3)
        ]
    )
    last_name = models.CharField(
        max_length=255,
        validators=[
            MinLengthValidator(3)
        ]
    )
    phone_number = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^\d{9}$',
            )
        ],
        help_text="فقط 10 رقم آخر شماره تلفن را وارد کنید."
    )

    def save(self, *args, **kwargs):
        if not self.phone_number.startswith('+98'):
            self.phone_number = f"+98{self.phone_number}"
        super().save(*args, **kwargs)

    email = models.EmailField(unique=True)
    password = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(9, message="رمز عبور باید حداقل ۸ کاراکتر باشد."),
            RegexValidator(
                regex=r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$',
                message='رمز عبور باید حداقل شامل یک حرف کوچک، یک حرف بزرگ، یک عدد و یک کاراکتر خاص باشد.'
            )
        ],
        help_text="رمز عبور باید حداقل ۸ کاراکتر و ترکیبی از حروف، اعداد و کاراکترهای خاص باشد."
    )

    birthday = models.DateField(null=True, blank=True)
    # @property
    # def discount(self):
    #     today = datetime.today()
    #     birth_day = self.birthday.day
    #     birth_month = self.birthday.month
    #     today_day = today.day
    #     today_month = today.month
    #
    #     if birth_day == today_day and birth_month == today_month:
    #         discount = 0.25
    #     else:
    #         discount = 0
    #     return discount

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    cafe_space_position = models.CharField(max_length=50)

    def __str__(self):
        return f"Table {self.table_number}"

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
