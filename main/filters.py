from django_filters import filters
from django_filters import FilterSet
from .models import Inventory, Work

class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'

# 在庫モデルフィルター
class InventoryFilter(FilterSet):

    name = filters.CharFilter(label='型式', lookup_expr='contains')
    serial_no = filters.CharFilter(label='号機', lookup_expr='contains')
    other_ja = filters.CharFilter(label='詳細／仕様', lookup_expr='contains')

    order_by = MyOrderingFilter(
        fields=(
            ('status', 'status'),
            ('company_id', 'company_id'),
            ('type_id', 'type_id'),
            ('manufacturer_id', 'manufacturer_id'),
            ('name', 'name'),
            ('year', 'year'),
            ('serial_no', 'serial_no'),
            ('hours', 'hours'),
        ),
        field_labels={
            'status': 'ステータス',
            'company_id': '会社',
            'type_id': '機械分類',
            'manufacturer_id': 'メーカー',
            'name': '型式',
            'year': '年式',
            'serial_no': '号機',
            'hours': '稼働時間',
        },
        label='並び順'
    )

    class Meta:
        model = Inventory
        fields = ('company_id', 'status', 'type_id', 'manufacturer_id', 'name', 'year', 'serial_no', 'hours', 'other_ja', 'buyer', 'order_pay_date', 'sell_pay_date', 'sell_month')

# 作業モデルフィルター
class WorkFilter(FilterSet):

    name = filters.CharFilter(label='作業名', lookup_expr='contains')

    order_by = MyOrderingFilter(
        fields=(
            ('status', 'status'),
            ('name', 'name'),
            ('machine_name', 'machine_name'),
            ('serial_no', 'serial_no'),
            ('client_id', 'client_id'),
        ),
        field_labels={
            'status': 'ステータス',
            'machine_name': '作業名',
            'serial_no': '号機',
            'machine_name': '型式',
            'client_id': '顧客',
        },
        label='並び順'
    )

    class Meta:
        model = Work
        fields = ('status', 'name', 'machine_name', 'serial_no', 'client_id')
