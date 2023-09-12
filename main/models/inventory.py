from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.contrib.auth.models import User
from django.urls import reverse

# 状態
CONDITION = (
    ('5','5：新車もしくは、新車に近い状態'),
    ('4','4：高年式・メーターの少ない極上品'),
    ('3','3：現状で使用可能な状態'),
    ('2','2：故障はしてないが、使用するには軽微な修理や整備が必要なもの'),
    ('1','1：故障はしていないが、摩耗が激しく、使用するには相当の修理や整備が必要なもの'),
    ('B','B：エンジンや油圧系統など重要部品が故障しているもの'),
)

# 整備状況
CONDITION_MAINTENANCE = (
    ('1','1：全塗装整備済み(Painted and Served)'),
    ('2','2：整備済み(Served)'),
    ('3','3：現状有姿(As is condition)'),
)

# ステータス
STATUS = (
    ('0','有効在庫'),
    ('1','締め在庫'),
    ('2','レンタル空車'),
    ('3','レンタル出庫中'),
    ('5','その他'),
    ('6','削除その他'),
    ('9','削除在庫'),
)

# Create your models here.
class Inventory(models.Model):
    id = models.AutoField(verbose_name="会社ID", primary_key=True)
    status = models.CharField(verbose_name="ステータス", choices=STATUS, max_length=2, default='0')
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, db_column='company_id', verbose_name="会社")
    name = models.CharField(verbose_name="型式/MODEL", max_length=256)
    price = models.IntegerField(verbose_name="表示価格/LIST PRICE",default=0)
    condition = models.CharField(verbose_name="程度/CONDITION RANK", choices=CONDITION, max_length=2, default='5')
    condition_maintenance = models.CharField(verbose_name="整備状況/CONDITION MAINTENANCE", choices=CONDITION_MAINTENANCE, max_length=2, default='1')
    type = models.ForeignKey('Type_Machine', on_delete=models.SET_NULL, null=True, db_column='machine_type_id', verbose_name="分類")
    manufacturer = models.ForeignKey('Maker', on_delete=models.SET_NULL, null=True, db_column='maker_id', verbose_name="メーカー/MANUFACTURER")
    year = models.CharField(verbose_name="年式/YEAR", blank=True, null=True, max_length=16)
    serial_no = models.CharField(verbose_name="号機", blank=True, null=True, max_length=256)
    hours = models.CharField(verbose_name="稼働時間", blank=True, null=True, max_length=16)
    other = models.CharField(verbose_name="DESCRIPTION", blank=True, null=True, max_length=256)
    other_ja = models.CharField(verbose_name="詳細／仕様", blank=True, null=True, max_length=256)
    pic_url = models.CharField(verbose_name="写真/PHOTO", blank=True, null=True, max_length=256)
    account = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="仕入担当")
    order_date = models.DateField(verbose_name="発注日", blank=True, null=True)
    web_disp = models.BooleanField(verbose_name="WEB表示", default=False)
    seller_name = models.CharField(verbose_name="仕入先名", blank=True, null=True, max_length=256)
    seller = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, verbose_name="仕入先", related_name="seller_client")
    order_price = models.IntegerField(verbose_name="仕入価格",default=0)
    order_trans_cost = models.IntegerField(verbose_name="仕入運賃",default=0)
    parts_cost = models.IntegerField(verbose_name="部品代",default=0)
    maintenance_cost = models.IntegerField(verbose_name="整備費",default=0)
    order_out_order_cost = models.IntegerField(verbose_name="仕入外注費",default=0)
    order_cost_price = models.IntegerField(verbose_name="仕入原価",default=0)
    tran_place = models.CharField(verbose_name="引渡場所", blank=True, null=True, max_length=256)
    sell_trance_cost = models.IntegerField(verbose_name="販売運賃",default=0)
    ship_cost = models.IntegerField(verbose_name="船積費用",default=0)
    sell_out_order_cost = models.IntegerField(verbose_name="販売外注費",default=0)
    ins_cost = models.IntegerField(verbose_name="保険料",default=0)
    freight_cost = models.IntegerField(verbose_name="フレイト",default=0)
    sell_cost_price = models.IntegerField(verbose_name="販売原価",default=0)
    sell_price = models.IntegerField(verbose_name="販売価格",default=0)
    whol_price = models.IntegerField(verbose_name="業販価格",default=0)
    profit = models.IntegerField(verbose_name="利益",default=0)
    buyer_name = models.CharField(verbose_name="販売先名", blank=True, null=True, max_length=256)
    buyer = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, verbose_name="販売先", related_name="buyer_client")
    order_pay_date = models.DateField(verbose_name="仕入代金支払日", blank=True, null=True)
    sell_pay_date = models.DateField(verbose_name="売上入金日", blank=True, null=True)
    sell_month = models.DateField(verbose_name="売上月", blank=True, null=True)
    memo = models.TextField(verbose_name="在庫メモ", blank=True, null=True)

    # レンタル専用用項目
    enrollment = models.CharField(verbose_name="在籍", blank=True, null=True, max_length=256)
    price_day = models.IntegerField(verbose_name="日単価",default=0)
    price_month = models.IntegerField(verbose_name="月単価",default=0)
    price_support = models.IntegerField(verbose_name="サポート料金",default=0)
    size = models.IntegerField(verbose_name="サイズ（㎥）",default=0)
    weight = models.IntegerField(verbose_name="重量（㎏）",default=0)

    creator = CurrentUserField(verbose_name="作成者", editable=False, related_name="create_inventory")
    created = models.DateTimeField(verbose_name="作成日", auto_now_add=True)
    modifier = CurrentUserField(verbose_name="更新者", editable=False, related_name="update_inventory", on_update=True, )
    modified = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return str(self.id) +':' + self.name

    def get_absolute_url(self):
        return reverse('inventory_list')
    
    class Meta:
        verbose_name = "在庫"
        verbose_name_plural = "在庫"