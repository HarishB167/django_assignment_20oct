from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from . import models, serializers

# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = models.User.objects \
        .prefetch_related('address', 'profile_picture').all()
    serializer_class = serializers.UserSerializer


# class PatientViewSet(ModelViewSet):
#     queryset = models.Patient.objects \
#         .select_related('user') \
#         .prefetch_related('user__address', 'user__profile_picture').all()
#     serializer_class = serializers.PatientSerializer


# class DoctorViewSet(ModelViewSet):
#     queryset = models.Doctor.objects. \
#         select_related('user') \
#         .prefetch_related('user__address', 'user__profile_picture').all()
#     serializer_class = serializers.DoctorSerializer


