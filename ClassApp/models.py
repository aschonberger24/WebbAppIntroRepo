from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User


# Create your models here.
class Currency(models.Model):
    iso = models.CharField(max_length=3)
    long_name = models.CharField(max_length=50)

    def __repr__(self):
        return self.iso + " " + self.long_name

    def __str__(self):
        return self.iso + " " + self.long_name


class Holding(models.Model):
    iso = models.ForeignKey(Currency, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    buy_date = models.DateField()

    def __repr__(self):
        return self.iso.iso + " " + str(self.value) + " " + str(self.buy_date)

    def __str__(self):
        return self.iso.long_name + " " + str(self.value) + " " + str(self.buy_date)


class Rates(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    x_currency = models.CharField(max_length=3)
    rate = models.FloatField(default=1.0)
    last_update_time = models.DateTimeField()

    def __repr__(self):
        return self.currency.iso + " " + self.x_currency + " " + str(self.rate)

    def __str__(self):
        return self.currency.iso + " " + self.x_currency + " " + str(self.rate)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id_num = models.IntegerField(default=0)
    title = models.CharField(max_length=250)
    ingredients = models.CharField(max_length=5000, default=None)  # ManyToManyField(Ingredient)
    # def __init__(self):
    #     self.ingredients = ()
    instructions = models.TextField()
    image = models.CharField(max_length=500)


    def __repr__(self):
        return str(self.id_num) + " " + self.title + " " + str(
            self.ingredients) + " " + self.instructions + " " + self.image

    def __str__(self):
        return str(self.id_num) + " " + self.title + " " + str(
            self.ingredients) + " " + self.instructions + " " + self.image


class AccountHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=None)
    recipes_viewed = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return self.user.username
