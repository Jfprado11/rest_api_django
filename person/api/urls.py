from django.urls import path
from .views import PersonApiList, PersonApiDetail

urlpatterns = [
    path('person/', PersonApiList.as_view()),
    path('person/<int:pk>', PersonApiDetail.as_view())
]
