from django_filters import filters
from django_filters import FilterSet

from .models import Inventory, Work, RentalOrder

class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'

# 在庫モデルフィルター
class InventoryFilter(FilterSet):

    name = filters.CharFilter(label='型式', lookup_expr='contains')
    serial_no = filters.CharFilter(label='号機', lookup_expr='contains')

    order_by = MyOrderingFilter(
        fields=(
            ('status', 'status'),
            ('company_id', 'company_id'),
            ('type_id', 'type_id'),
            ('manufacturer_id', 'manufacturer_id'),
            ('name', 'name'),
            ('serial_no', 'serial_no'),
            ('seller', 'seller'),
            ('buyer', 'buyer'),
            ('order_pay_date', 'order_pay_date'),
            ('sell_pay_date', 'sell_pay_date'),
            ('sell_month', 'sell_month'),
        ),
        field_labels={
            'status': 'ステータス',
            'company_id': '会社',
            'type_id': '機械分類',
            'manufacturer_id': 'メーカー',
            'name': '型式',
            'serial_no': '号機',
            'seller': '仕入先',
            'buyer': '販売先',
            'order_pay_date': '仕入代金支払日',
            'sell_pay_date': '売上入金日',
            'sell_month': '売上月',
        },
        label='並び順'
    )

    class Meta:
        model = Inventory
        fields = ('company_id', 'status', 'type_id', 'manufacturer_id', 'name', 'serial_no', 'seller', 'buyer')

# 作業モデルフィルター
class WorkFilter(FilterSet):

    name = filters.CharFilter(label='作業名', lookup_expr='contains')

    order_by = MyOrderingFilter(
        fields=(
            ('status', 'status'),
            ('name', 'name'),
            ('work_inventory', 'work_inventory'),
            ('client_id', 'client_id'),
        ),
        field_labels={
            'status': 'ステータス',
            'name': '作業名',
            'work_inventory': '機種-型-号機',
            'client_id': '顧客',
        },
        label='並び順'
    )

    class Meta:
        model = Work
        fields = ('status', 'name', 'work_inventory', 'client_id')

# レンタル注文モデルフィルター
class RentalOrderFilter(FilterSet):

    order_by = MyOrderingFilter(
        fields=(
            ('out_date', 'out_date'),
            ('in_date', 'in_date'),
            ('start_date', 'start_date'),
            ('end_date', 'end_date'),
            ('close_date', 'close_date'),
        ),
        field_labels={
            'out_date': '出庫日',
            'in_date': '返却日',
            'start_date': 'レンタル開始日',
            'end_date': 'レンタル終了日',
            'close_date': '締め日',
        },
        label='並び順'
    )

    class Meta:
        model = RentalOrder
        fields = ['rental_inventory','client','order_type','close_date']
