from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.paginait, name='paginait'),
    path('postari/<int:pkit_id>', views.postari, name='postari'),


]
