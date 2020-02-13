from django.db import models
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['fname']) < 2:
            errors['fname'] = "First Name needs to be longer"
        if len(data['lname']) < 2:
            errors['lname'] = "Last Name needs to be longer"
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = "Email is invalid"
        if len(data['password']) < 8:
            errors['password'] = "Password must be 8 characters or longer"
        if data['password'] != data['cpassword']:
            errors['password'] = "Passwords do not match"
        return errors


class ItemManager(models.Manager):
    def validator(self, data):
        errors = {}
        if data['image_link'] == "":
            errors['profile'] = "Must have image url"
            return errors


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Item(models.Model):
    quantity = models.IntegerField()
    is_requested = models.BooleanField(default=False)
    image_link = models.TextField()
    is_low_inventory = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
    last_updated_by = models.OneToOneField(to=User, on_delete='CASCADE')
    votes = models.ManyToManyField("Vote", related_name="item_votes")


class ItemsToOrder(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=True)
    items = models.ForeignKey(
        Item, on_delete='CASCADE', related_name="Items_In_Queue")


class OrderHistory(models.Model):
    quantity_ordered = models.IntegerField()
    date_replenished = models.DateTimeField(auto_now=True)
