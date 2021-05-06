from django.urls import path
from . import views


urlpatterns = [
    path("<str:audioFileType>/", views.get, name="get"),
    path("<str:audioFileType>/<int:id>", views.get, name="get"),
    path("home", views.home, name="home"),
    path("create/<str:audioFileType>/", views.create, name= "create"),
    path("update/<str:audioFileType>/<int:id>", views.update, name= "update"),
    path("delete/<str:audioFileType>/<int:id>", views.delete, name= "delete"),
]