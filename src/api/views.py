from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from src.accounts.models import User
from .serializers import (
    UserPasswordChangeSerializer, UserSerializer,
    CaptureSerializer, PlantSerializer, DiseaseSerializer, CanopySerializer)

from .models import (
    Plant, Disease, Capture,
    Canopy
)

""" AUTH USER API' S """


class UserPublicDetailedView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileDetailedView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserPasswordChangeView(generics.UpdateAPIView):
    model = User
    serializer_class = UserPasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


""" CAPTURES """


class CaptureListView(generics.ListCreateAPIView):
    serializer_class = CaptureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Capture.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CaptureGetPutDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        capture = get_object_or_404(Capture.objects.filter(user=self.request.user), pk=self.kwargs['pk'])
        return capture

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


""" PUBLIC API'S """


class PlantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.AllowAny]


class DiseaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination


class CanopyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Canopy.objects.all()
    serializer_class = CanopySerializer
    permission_classes = [permissions.AllowAny]


