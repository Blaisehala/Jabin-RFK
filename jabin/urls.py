from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('about/',views.about, name = 'about-page'),
    path('programs/',views.programs,name = 'programs'),
    path('data/',views.data,name = 'data'),
    path('contact/',views.contact,name = 'contact'),
    
]