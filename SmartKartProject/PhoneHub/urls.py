from django.urls import path
from .views import addPhone, updatePhone, deletePhone, showPhone

urlpatterns=[
    path("add/",addPhone, name="add-phone"),
    path("Update/<i>/",updatePhone, name="update-phone"),
    path("Delete/<i>/",deletePhone, name="delete-phone"),
    path("show/",showPhone, name="show-phone"),
]