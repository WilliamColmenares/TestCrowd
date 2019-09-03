from django.contrib import admin
from django.urls import path, include
from pets.views import pet_list, user_login, create_pet, update_pet, delete_pet, logout_view
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('dashboard/', pet_list, name='pet_list'),
    path('', user_login, name='user_login'),
    path('update/<int:id>/', update_pet, name='update_pet'),
    path('delete/<int:id>', delete_pet, name='delete_pet'),
    path('add/', create_pet, name='create_pet'),
    path('logout/', logout_view, name='logout_view'),
    path('login-api/', obtain_jwt_token),
]
