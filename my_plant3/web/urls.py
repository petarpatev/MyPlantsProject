from django.urls import path, include

from my_plant3.web.views import index, show_catalogue, plant_create, plant_edit, plant_delete, plant_details, \
    profile_create, profile_edit, profile_delete, profile_details

urlpatterns = (
    path('', index, name='home page'),
    path('catalogue/', show_catalogue, name='show catalogue'),
    path('create/', plant_create, name='plant create'),
    path('edit/<int:pk>/', plant_edit, name='plant edit'),
    path('delete/<int:pk>/', plant_delete, name='plant delete'),
    path('details/<int:pk>/', plant_details, name='plant details'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
        path('details/', profile_details, name='profile details'),
    ])),

)
