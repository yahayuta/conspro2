from ..models import Inventory
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.urls import reverse_lazy

from ..filters import InventoryFilter
from ..service import inventory_xls_handler
from ..forms import InventoryEditForm

# 検索一覧画面
class InventoryFilterView(LoginRequiredMixin, FilterView):
    model = Inventory
    filterset_class = InventoryFilter
    queryset = Inventory.objects.all().order_by('-created')
    strict = False
    paginate_by = 5
    template_name = 'inventory_list.html'

    # 検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

# 一覧画面
class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventory_list.html'
    paginate_by = 5

# 新規作成
class InventoryCreateView(LoginRequiredMixin, CreateView):
    form_class = InventoryEditForm
    template_name = 'inventory_edit.html'
    model = Inventory

# 更新
class InventoryUpdateView(LoginRequiredMixin, UpdateView):
    form_class = InventoryEditForm
    template_name = 'inventory_edit.html'
    model = Inventory
    
# 削除
class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'inventory_edit.html'
    model = Inventory
    success_url = reverse_lazy('inventory_list')

# 発注書出力
@login_required
def download_ordersheet(request, id):
    return inventory_xls_handler.create_ordersheet(id)

# 請求書出力
@login_required
def download_jpinvoice(request):
    inventory_ids = request.POST.getlist('inventory_ids')
    return inventory_xls_handler.create_jpinvoice(inventory_ids)

# Proforma Invoice出力
@login_required
def download_proforma_invoice(request):
    inventory_ids = request.POST.getlist('inventory_ids')
    return inventory_xls_handler.create_proforma_invoice(inventory_ids)
