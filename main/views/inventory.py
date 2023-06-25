from ..models import Inventory
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.urls import reverse_lazy

from ..filters import InventoryFilter
from ..service import inventory_xls_handler

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
    fields = [
        'company',
        'name',
        'price',
        'condition',
        'condition_maintenance',
        'type',
        'manufacturer',
        'year',
        'serial_no',
        'hours',
        'other',
        'other_ja',
        'pic_url',
        'account',
        'order_date',
        'web_disp',
        'seller_name',
        'seller',
        'order_price',
        'order_trans_cost',
        'parts_cost',
        'maintenance_cost',
        'order_out_order_cost',
        'order_cost_price',
        'tran_place',
        'sell_trance_cost',
        'ship_cost',
        'sell_out_order_cost',
        'ins_cost',
        'freight_cost',
        'sell_cost_price',
        'sell_price',
        'whol_price',
        'profit',
        'buyer_name',
        'buyer',
        'order_pay_date',
        'sell_pay_date',
        'sell_month',
        'memo',        
        ]

# 更新
class InventoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'inventory_edit.html'
    model = Inventory
    fields = [
        'company',
        'name',
        'price',
        'condition',
        'condition_maintenance',
        'type',
        'manufacturer',
        'year',
        'serial_no',
        'hours',
        'other',
        'other_ja',
        'pic_url',
        'account',
        'order_date',
        'web_disp',
        'seller_name',
        'seller',
        'order_price',
        'order_trans_cost',
        'parts_cost',
        'maintenance_cost',
        'order_out_order_cost',
        'order_cost_price',
        'tran_place',
        'sell_trance_cost',
        'ship_cost',
        'sell_out_order_cost',
        'ins_cost',
        'freight_cost',
        'sell_cost_price',
        'sell_price',
        'whol_price',
        'profit',
        'buyer_name',
        'buyer',
        'order_pay_date',
        'sell_pay_date',
        'sell_month',
        'memo',        
        ]
# 削除
class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'inventory_edit.html'
    model = Inventory
    success_url = reverse_lazy('inventory_list')

# 発注書出力
@login_required
def download_ordersheet(request, id):
    return inventory_xls_handler.create_ordersheet(id)