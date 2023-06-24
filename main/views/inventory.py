from ..models import Inventory
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.urls import reverse_lazy

from ..filters import InventoryFilter

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
    template_name = 'inventory_edit.html'
    model = Inventory
    fields = ['type', 'manufacturer', 'name', 'year', 'serial_no', 'hours', 'other_ja', 'memo' ]

# 更新
class InventoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'inventory_edit.html'
    model = Inventory
    fields = ['type', 'manufacturer', 'name', 'year', 'serial_no', 'hours', 'other_ja', 'memo' ]

# 削除
class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'inventory_edit.html'
    model = Inventory
    success_url = reverse_lazy('inventory_list')