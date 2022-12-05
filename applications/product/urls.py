from django.urls import path
from applications.product.views import ProductListCreateApiView, ProducRetrieveUpdateDestroyApiView

urlpatterns = [
    path('', ProductListCreateApiView.as_view()),
    path('<int:pk>/', ProducRetrieveUpdateDestroyApiView.as_view()),
    # path('list/', ProductListApiView.as_view()),
    # path('create/', ProductCreateApiView.as_view()),
    # path('<int:pk>/', ProductDetailApiView.as_view())
]