from django.urls import path
from .views import LostObjectListCreateAPIView, LostObjectRetrieveAPIView

urlpatterns = [
    path('objects/', LostObjectListCreateAPIView.as_view(),
         name='lost-object-list'),
    path('objects/<int:id>/', LostObjectRetrieveAPIView.as_view(),
         name='lost-object-detail'),
]
