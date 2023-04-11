from django.shortcuts import render
from rest_framework import generics, permissions
from . models import Profile
from .serializer import ProfileSeralizer
from raknaren_drf.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSeralizer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileDetailer(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSeralizer
    permission_classes = [IsOwnerOrReadOnly]