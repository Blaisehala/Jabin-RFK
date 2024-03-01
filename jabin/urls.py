from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('donate/', views.donate, name='donate'),
    path('donate/',views.donate, name = 'donate'),
    path('about/',views.about, name = 'about-page'),
    path('programs/',views.programs,name = 'programs'),
    path('data/',views.data,name = 'data'),
    path('contact/',views.contact,name = 'contact'),
    path('stats/', views.stats, name='stats'),
    path('tools/', views.tools, name='tools'),
    
]