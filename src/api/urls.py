from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [

    path('user/<int:pk>/', views.UserPublicDetailedView.as_view(), name='user-view'),
    path('my/profile/', views.UserProfileDetailedView.as_view(), name='profile-info-view-update'),
    path('my/password/change/', views.UserPasswordChangeView.as_view(), name='user-password-chang-put'),

    path('capture/', views.CaptureListView.as_view(), name='capture-list-view'),
    path('capture/<int:pk>/', views.CaptureGetPutDeleteView.as_view(), name='capture-get-update-delete-view'),

]
