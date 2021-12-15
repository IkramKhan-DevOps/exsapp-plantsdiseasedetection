from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'plant', views.PlantViewSet)
router.register(r'disease', views.DiseaseViewSet)
router.register(r'canopy', views.CanopyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:pk>/', views.UserPublicDetailedView.as_view(), name='user-view'),
    path('my/profile/', views.UserProfileDetailedView.as_view(), name='profile-info-view-update'),
    path('my/password/change/', views.UserPasswordChangeView.as_view(), name='user-password-chang-put'),

    path('capture/', views.CaptureListView.as_view(), name='capture-list-view'),
    path('capture/<int:pk>/', views.CaptureGetPutDeleteView.as_view(), name='capture-get-update-delete-view'),

]
