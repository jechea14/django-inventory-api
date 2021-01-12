from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('category', views.CategoryView)
# router.register('product', views.ProductView)

urlpatterns = [
    # path('', include(router.urls))
    path('', views.apiOverview, name="api-overview"),
    path('product/', views.productList, name="product-list"),
    path('product/<str:pk>/', views.productDetail, name="product-detail"),
    path('product-create/', views.productCreate, name="product-create"),
    path('product-update/<str:pk>/', views.productUpdate, name="product-update"),
    path('product-delete/<str:pk>/', views.productDelete, name="product-delete"),
    
    path('category/', views.categoryList, name="category-list"),
    path('category/<str:pk>/', views.categoryDetail, name="category-detail"),
    path('category-create/', views.categoryCreate, name="category-create"),
    path('category-update/<str:pk>/', views.categoryUpdate, name="category-update"),
    path('category-delete/<str:pk>/', views.categoryDelete, name="category-delete"),
]