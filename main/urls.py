from django.urls import path

from .views import login, inventory

urlpatterns = [
    path('login/', login.login_view, name='login'),
    path('logout/', login.logout_view, name='logout'),
    path('top/', login.top_view, name='top'),
    path('inventory/', inventory.InventoryFilterView.as_view(), name="inventory_list"),
    path('inventory/new/', inventory.InventoryCreateView.as_view(), name='inventory_new'),
    path('inventory/edit/<int:pk>/', inventory.InventoryUpdateView.as_view(), name='inventory_edit'),
    path('inventory/delete/<int:pk>/', inventory.InventoryDeleteView.as_view(), name='inventory_delete'),
    path('inventory/download_ordersheet/<int:id>/', inventory.download_ordersheet, name='inventory_download_ordersheet'),
    path('inventory/download_jpinvoice/', inventory.download_jpinvoice, name='inventory_download_ordersheet'),
]