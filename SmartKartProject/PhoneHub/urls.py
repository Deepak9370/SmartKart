from django.template.defaultfilters import first
from django.urls import path
from .views import first_view, addPhone, updatePhone, deletePhone, showPhone, aboutView, servicesView, faqView

urlpatterns=[
    path("first/",first_view),
    path("add/",addPhone, name="add-phone"),
    path("Update/<i>/",updatePhone, name="update-phone"),
    path("Delete/<i>/",deletePhone, name="delete-phone"),
    path("show/",showPhone, name="show-phone"),
    path("about/",aboutView, name="about"),
    path("services/",servicesView, name="services"),
    path("faq/",faqView, name="faq"),
]