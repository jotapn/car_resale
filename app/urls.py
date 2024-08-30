from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view, new_car_view
from accounts.views import register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('cars/', cars_view, name='cars_list'),
    path('new_cars/', new_car_view, name='new_car'),
    path('', lambda request: redirect('/cars')),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

