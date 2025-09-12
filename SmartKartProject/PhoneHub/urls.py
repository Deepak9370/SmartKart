from django.template.defaultfilters import first
from django.urls import path
from .views import home, addPhone, updatePhone, deletePhone, showPhone, aboutView, servicesView, faqView, contactView

urlpatterns=[
    path("",home, name="home"),
    path("add/",addPhone, name="add-phone"),
    path("Update/<i>/",updatePhone, name="update-phone"),
    path("Delete/<i>/",deletePhone, name="delete-phone"),
    path("show/",showPhone, name="show-phone"),
    path("about/",aboutView, name="about"),
    path("services/",servicesView, name="services"),
    path("faq/",faqView, name="faq"),
    path("contact/",contactView, name="contact"),

]