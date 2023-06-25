import openpyxl
import datetime
import time

from ..models import Inventory
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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

@login_required
def download_ordersheet(request, id):
    print(id)

    inventory = Inventory.objects.get(pk=id)
    company = inventory.company
    print(company)

    # Excelのテンプレートファイルの読み込み
    wb = openpyxl.load_workbook('/django/main/static/tpl/OrderSheet.xlsx')

    sheet = wb['注文書']
    sheet['J1'] = id
    sheet['J2'] = datetime.date.today()

    sheet['K5'] = company.name
    sheet['K6'] = f"〒 {str(company.zip)[0:3]}-{str(company.zip)[3:]}"
    sheet['K7'] = company.address
    sheet['K9'] = f"電話：{company.tel}　FAX：{company.fax}"

    seller = inventory.seller

    sheet['B5'] = seller.name + " 御中"
    sheet['B7'] = f"〒 {str(seller.zip)[0:3]}-{str(seller.zip)[3:]}"
    sheet['B8'] = seller.address
    sheet['B10'] = sheet['K9'] = f"電話：{seller.tel}　FAX：{seller.fax}"

    sheet['B23'] = inventory.name
    sheet['B24'] = inventory.serial_no
    sheet['H23'] = inventory.order_price

    # Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % str(inventory.name) + '_' + str(time.time()) + '.xlsx'

    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    # 生成したHttpResponseをreturnする
    return response