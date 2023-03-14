from django.urls import path
from . import views



urlpatterns = [
    path('', views.crud_view1, name="crud_view1"),

    path("update_schedular/<str:s>/", views.update_schedular, name="update_schedular"),
    path("delete_schedular/<str:s>/", views.delete_schedular, name="delete_schedular"),

    path('entry/',views.entry,name="entry"),
    path('entry/csvinput',views.csvinput,name="csvinput"),
]