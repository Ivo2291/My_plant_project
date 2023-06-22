from django.urls import path, include

from My_plant_project.my_plant_app.views import index, catalogue_page, profile_create_page, profile_details_page, \
    profile_edit_page, profile_delete_page, plant_create_page, plant_details_page, plant_edit_page, plant_delete_page


urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue_page, name='catalogue'),
    path('profile/', include([
        path('create/', profile_create_page, name='profile create'),
        path('details/', profile_details_page, name='profile details'),
        path('edit/', profile_edit_page, name="profile edit"),
        path('delete/', profile_delete_page, name="profile delete"),
    ])),

    path('create/', plant_create_page, name='plant create'),
    path('details/<int:pk>/', plant_details_page, name='plant details'),
    path('edit/<int:pk>/', plant_edit_page, name="plant edit"),
    path('delete/<int:pk>/', plant_delete_page, name="plant delete"),
)
