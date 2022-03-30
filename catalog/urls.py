from django.contrib import admin
from django.urls import path, include
from catalog import views

app_name = "catalog"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.mainview, name='main'),
    path('item_delete=<int:pk>/', views.ItemDeleteView.as_view(), name='delete' ),
    path('item_edit=<int:pk>/', views.ItemUpdateView.as_view(), name='edit' ),


]