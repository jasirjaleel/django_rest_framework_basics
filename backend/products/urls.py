from django.urls import path
from .views import ProductListCreateAPIView, ProductMixinView, ProductDestroyAPIView, ProductUpdateAPIView
    
urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('<int:pk>/', ProductMixinView.as_view()),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view()),
    path('<int:pk>/destroy/', ProductDestroyAPIView.as_view()),
]
