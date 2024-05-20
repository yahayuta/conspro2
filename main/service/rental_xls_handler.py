import openpyxl
import datetime
import time

from django.http import HttpResponse
from ..models import RentalOrder

# 出庫・返却伝票出力
def create_rental_ordersheet(rentaL_order_id):
    rentaL_order = RentalOrder.objects.get(pk=rentaL_order_id)
    company = rentaL_order.company
    print(company)

    # Excelのテンプレートファイルの読み込み
    wb = openpyxl.load_workbook('/django/main/static/tpl/RentalOrderSheet.xlsx')

    sheet = wb['出庫・返却伝票']

    sheet['J6'] = company.name
    sheet['J7'] = company.address
    sheet['j8'] = f"TEL : {company.tel}"
    sheet['j9'] = f"FAX : {company.fax}"

    client = rentaL_order.client

    sheet['A5'] = f"{client.name}　御中"
    sheet['A6'] = f"{client.office}　様"
    sheet['B8'] = f"{client.tel}"
    sheet['B9'] = f"{client.fax}"

    sheet['E11'] = f"{rentaL_order.rental_inventory.name}　・　{rentaL_order.rental_inventory.serial_no}"
    sheet['E12'] = rentaL_order.order_place
    sheet['E13'] = rentaL_order.order_name

    if rentaL_order.order_type == "0":
        sheet['E14'] = rentaL_order.rental_inventory.price_day
    if rentaL_order.order_type == "1":
        sheet['E14'] = rentaL_order.rental_inventory.price_month

    sheet['E15'] = rentaL_order.out_date
    sheet['E17'] = rentaL_order.hours_start
    sheet['E18'] = rentaL_order.start_date
    sheet['E19'] = rentaL_order.rental_inventory.price_support

    # Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % str(rentaL_order_id) + '_' + str(time.time()) + '.xlsx'
    
    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    return response
