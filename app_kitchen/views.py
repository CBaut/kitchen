from django.shortcuts import render, redirect
from .models import *
from datetime import datetime

# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, "index.html")


def item_new(request):
    if request.method == 'GET':
        return render(request, "item_new.html")


def item_all(request):
    if request.method == 'GET':
        return render(request, "item_all.html")


def item_view(request):
    if request.method == 'GET':
        # Render item view
        return render(request, "item_view.html")
    # Delete selected item
    if request.method == 'DELETE':
        return redirect("/")


def item_edit(request):
    if request.method == 'GET':
        # Rendering edit view page
        return render(request, "item_edit.html")
    # Updating the item
    if request.method == 'PUT':
        return redirect("/")


def items(request):
    if request.method == 'GET':
        print("Getting all items")
        return render(request, "items.html")

    if request.method == 'POST':
        errors = Item.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/items/new')

    # user_submitted = User.objects.get(id=user_id)

    new_item = Item.objects.create(
        name=request.POST['name'],
        image_link=request.POST['image_link'],
        quantity=request.POST['quantity'],
        # last_updated_by=user_submitted
    )

    print("Create a new item")
    return redirect("/")


def log_reg(request):
    if request.method == 'GET':
        return render(request, "log_reg.html")


def login(request):
    if request.method == 'POST':
        return redirect("/")


def register(request):
    if request.method == 'POST':
        return redirect("/")


def order_new(request):
    if request.method == 'GET':
        return render(request, "order_new.html")


def order_all(request):
    if request.method == 'POST':
        return redirect("/")
    return render(request, "order_all.html")


def order_view(request):
    if request.method == 'GET':
        # Render order view
        return render(request, "order_view.html")

    # Delete selected order
    if request.method == 'DELETE':
        return redirect("/")


def order_edit(request):
    if request.method == 'GET':
        # Rendering edit view page
        return render(request, "order_edit.html")

    # Updating the order
    if request.method == 'PUT':
        return redirect("/")
