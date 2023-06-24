from django.urls import path

from .views import login, inventory

urlpatterns = [
    path('login/', login.login_view, name='login'),
    path('logout/', login.logout_view, name='logout'),
    path('top/', login.top_view, name='top'),
    path('inventory/', inventory.InventoryFilterView.as_view(), name="inventory_list"),
    path('inventory/new/', inventory.InventoryCreateView.as_view(), name='inventory_new'),
    path('inventory/edit/<int:pk>/', inventory.InventoryUpdateView.as_view(), name='inventory_edit'),
    path('inventory/delete/<int:pk>/', inventory.InventoryDeleteView.as_view(), name='inventory_delete')
]