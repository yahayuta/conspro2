from django.urls import path

from .views import login
from .views import inventory
from .views import work
from .views import rental

urlpatterns = [
    path('login/', login.login_view, name='login'),
    path('logout/', login.logout_view, name='logout'),
    path('top/', login.top_view, name='top'),
    path('inventory/', inventory.InventoryFilterView.as_view(), name="inventory_list"),
    path('inventory/new/', inventory.InventoryCreateView.as_view(), name='inventory_new'),
    path('inventory/edit/<int:pk>/', inventory.InventoryUpdateView.as_view(), name='inventory_edit'),
    path('inventory/delete/<int:pk>/', inventory.InventoryDeleteView.as_view(), name='inventory_delete'),
    path('inventory/download_ordersheet/<int:id>/', inventory.download_ordersheet, name='inventory_download_ordersheet'),
    path('inventory/download_jpinvoice/', inventory.download_jpinvoice, name='download_jpinvoice'),
    path('inventory/download_proforma_invoice/', inventory.download_proforma_invoice, name='download_proforma_invoice'),
    path('work/', work.WorkFilterView.as_view(), name='work_list'),
    path('work/new/', work.work_new, name='work_new'),
    path('work/edit/<int:pk>/', work.work_edit, name='work_edit'),
    path('work/download_invoice/<int:id>/', work.download_invoice, name='work_download_invoice'),
    path('rental_order/', rental.RentalOrderFilterView.as_view(), name='rental_order_list'),
    path('rental_order/new/', rental.rental_order_new, name='rental_order_new'),
    path('rental_order/edit/<int:pk>/', rental.rental_order_edit, name='rental_order_edit'),
    path('rental_order/download_rental_ordersheet/<int:id>/', rental.download_rental_ordersheet, name='download_rental_ordersheet'),
    path('rental_order/download_rental_invoice/<int:id>/', rental.download_rental_invoice, name='download_rental_invoice'),
]
