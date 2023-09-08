from rest_framework import generics
from backend.permissions import IsOwnerOrReadOnly
from .models import Admins
from .serializers import ProfileSerializer


class AdminsList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Admins.objects.all()
    serializer_class = AdminsSerializer


class AdminsDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Admins.objects.all()
    serializer_class = AdminsSerializer