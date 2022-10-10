


from django.urls import path
from . import views
import os
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('map',views.showmap,name='map')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    