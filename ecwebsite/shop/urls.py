from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "index"),
    path("about/",views.about, name = "aboutUs"),
    path("contact",views.contact, name = "contactUs"),
    path("tracker/",views.tracker, name = "trackingStatus"),
    path("productview/",views.productview, name = "productview"),
    path("search/",views.search, name = "search"),
    path("checkout/",views.about, name = "checkout"),
    path("temp/",views.temp, name="temp"),
]