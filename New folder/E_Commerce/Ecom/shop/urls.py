from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="Shop Home"),
    path("contact/",views.Contact,name="ContactUs"),
    path("tracker/",views.Tracker,name="Track Your Order"),
    path("search/",views.Search,name="Search"),
    path("productviews/",views.prodview,name="Product View"),
    path("about/",views.about,name="About Us"),
    path("Checkout/",views.check,name="CheckOut")
]