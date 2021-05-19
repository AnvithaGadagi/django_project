from django.urls import path
from . import views


urlpatterns = [
    # get all data- /song or /podcast or /audiobook
    path("<str:audioFileType>/", views.get, name="get"),
    # get specific data- /song/1 or /podcast/1 or /audiobook/1
    path("<str:audioFileType>/<int:id>", views.get, name="get"),
    # create/add data- /create/song or /create/podcast or /create/audiobook
    path("create/<str:audioFileType>/", views.create, name="create"),
    # update existing data- /update/song/1 or /update/podcast/1 or /update/audiobook/1
    path("update/<str:audioFileType>/<int:id>", views.update, name="update"),
    # delete data- /delete/song/1 or /delete/podcast/1 or /delete/audiobook/1
    path("delete/<str:audioFileType>/<int:id>", views.delete, name="delete"),
    path("home/", views.home, name="home"),
]