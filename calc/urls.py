from django.template.context_processors import static
from calc import admin

from telusko import settings
from . import views
from django.urls import path
from django.templatetags.static import static

app_name = 'calc'

urlpatterns = [
    
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('stoke/', views.stoke, name='stoke'),
    path('Sold/', views.Sold, name='Sold'),
    path('oldtractor/', views.oldtractor, name='oldtractor'),
    path('about/', views.about, name='about'),
    path('inspection/<int:pk>/', views.inspection, name='inspection'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout/", views.logout_user, name='logout'),
    path("Contactus/", views.Contact_us, name='contactus'),
    path("OurTeam/", views.Our_Team, name='ourteam'),
    path("Customer/", views.Happy_customer, name='customer'),
    path("saveenquiry/", views.SaveCustomer, name='save-enquiry'),
    path("gallery/", views.Gallery, name='gallery'),
    path("addtractor/", views.Add_Tractor, name='addtractor'),
    path("addgallery/", views.Add_Gallery, name='addgallery'),

]

+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 