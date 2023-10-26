cdfrom django.db import models

# Create your models here.
class User(models.Model):
    _id = models.AutoField(verbose_name='Айді користувача', primary_key=True, blank=False)
    username = models.TextField(verbose_name="Юзернем")
    password = models.TextField(verbose_name="Пapoль")
    payments_data = models.TextField(verbose_name="Kapтoчka")
    delivery_data = models.TextField()
    phone = models.TextField()
    email = models.EmailField()

    def __str__(self):
        print(f"{self._id} - {self.username}")
        return f"{self._id} - {self.username}"

class Category(models.Model):
    _id = models.AutoField (primary_key=True) 
    category_name = models.TextField()
    
    def __repr__ (self):
        print(f" {self.category_name}")
        return f"{self.category_name}"

class Product (models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    small_description = models.CharField(max_length=30)
    count = models.IntegerField()
    image = models.ImageField()

    def __repr__ (self):
        return f"{self.name}"

class Order (models.Model):
    _id = models.AutoField(primary_key = True)
    import datetime 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    delivery_info = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    status = models.TextField()

    def __repr__(self):
        return f"{self._id}-{self.status}-{self.date}"

class Reviews (models.Model):
    from django.core.validators import MaxValueValidator, MinValueValidator
    _id = models.AutoField (primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(default=0, validators=[MinValueValidator (1), MaxValueValidator (5)])
    mark_text = models.TextField()
    