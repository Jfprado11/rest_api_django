from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from person.models import Person
from .serializers import PersonSerializer


class PersonApiList(generics.ListCreateAPIView):
    """
    Will prepare the view for the Person model. this part is the
    Create and Read all objects
    """
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonApiDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Will prepare the view for the person model. it does the retrive object by its pk
    destroy the object and also can updated
    """
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
