from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name="Index"),
    path('familiar/<int:familiar_id>', views.familiar_por_id, name='familiar_por_id')
]


