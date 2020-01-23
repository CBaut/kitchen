import app_kitchen.views
from django.urls import path, include

from django.contrib import admin

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", app_kitchen.views.index, name="index"),
    path("items/new/", app_kitchen.views.item_new, name="item_new"),
    path("items/:id/edit/", app_kitchen.views.item_edit, name="item_edit"),
    path("items/:id/", app_kitchen.views.item_view, name="item_view"),
    path("items/", app_kitchen.views.items, name="items"),
    path("logreg/", app_kitchen.views.log_reg, name="log_reg"),
    path("log/", app_kitchen.views.login, name="login"),
    path("reg/", app_kitchen.views.register, name="register"),
    path("orders/new/", app_kitchen.views.order_new, name="order_new"),
    path("orders/", app_kitchen.views.order_all, name="order_all"),
    path("orders/:id/", app_kitchen.views.order_view, name="order_view"),
    path("orders/:id/edit", app_kitchen.views.order_edit, name="order_edit")
    # path("db/", app_kitchen.views.db, name="db"),
    # path("admin/", admin.site.urls),
]
