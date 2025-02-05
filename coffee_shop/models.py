from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
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
    phone_number = models.CharField(max_length=15)
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

    @property
    def discount(self):
        today = datetime.today()
        birth_day = self.birthday.day
        birth_month = self.birthday.month
        today_day = today.day
        today_month = today.month

        if birth_day == today_day and birth_month == today_month:
            discount = 0.25
        else:
            discount = 0
        return discount

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


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menuitem_set')
    discount = models.IntegerField(null=True, blank=True, default=0,
                                   validators=[MinValueValidator(0), MaxValueValidator(99)])
    description = models.TextField(null=True, blank=True)
    serving_time_period = models.CharField(max_length=50, null=True, blank=True)
    estimated_cooking_time = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)


class Comment(models.Model):
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='comment_set')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True, related_name='orders')
    menu_items = models.ManyToManyField(MenuItem, through='OrderItem')
    ready = models.BooleanField(default=False)  # choose
    timestamp = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.table} {self.menu_items} {self.ready} {self.timestamp}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitem_set', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"


class Receipt(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        total_price = 0
        for i in self.order.orderitem_set.all():
            item = i.menu_item
            if item.discount == 0:
                total_price += item.price * i.quantity
            else:
                discounted_price = item.price - (item.price * (item.discount / 100))
                total_price += discounted_price * i.quantity
        return total_price

    @property
    def vat(self):
        return self.total_price * (10 / 100)

    @property
    def final_price(self):
        return self.total_price + self.vat

    def save(self, *args, **kwargs):
        """قبل از ذخیره، مقدار total_price را محاسبه می‌کند"""
        super().save(*args, **kwargs)


class Payment(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Receipt {self.receipt.id}"
