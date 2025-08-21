from django.template.defaultfilters import first
from django.urls import path
from .views import first_view, addPhone, updatePhone, deletePhone, showPhone

urlpatterns=[
    path("first/",first_view),
    path("add/",addPhone, name="add-phone"),
    path("Update/<i>/",updatePhone, name="update-phone"),
    path("Delete/<i>/",deletePhone, name="delete-phone"),
    path("show/",showPhone, name="show-phone"),
]