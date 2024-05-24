import openpyxl
import datetime
import time

from django.http import HttpResponse
from ..models import RentalOrder, RentalOrderRow

# 出庫・返却伝票出力
def create_rental_ordersheet(rental_order_id):
    rental_order = RentalOrder.objects.get(pk=rental_order_id)
    company = rental_order.company
    print(company)

    # Excelのテンプレートファイルの読み込み
    wb = openpyxl.load_workbook('/django/main/static/tpl/RentalOrderSheet.xlsx')

    sheet = wb['出庫・返却伝票']

    sheet['J6'] = company.name
    sheet['J7'] = company.address
    sheet['j8'] = f"TEL : {company.tel}"
    sheet['j9'] = f"FAX : {company.fax}"

    client = rental_order.client

    sheet['A5'] = f"{client.name}　御中"
    sheet['A6'] = f"{client.office}　様"
    sheet['B8'] = f"{client.tel}"
    sheet['B9'] = f"{client.fax}"

    sheet['E11'] = f"{rental_order.rental_inventory.name}　・　{rental_order.rental_inventory.serial_no}"
    sheet['E12'] = rental_order.order_place
    sheet['E13'] = rental_order.order_name

    rental_order_rows = rental_order.rental_order_id.all()
    sheet['E14'] = rental_order_rows[0].price

    sheet['E15'] = rental_order.out_date
    sheet['E16'] = rental_order.hours_start
    sheet['E17'] = rental_order_rows[2].price
    sheet['E18'] = rental_order.start_date
    sheet['E19'] = rental_order.rental_inventory.price_support

    # Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % str(rental_order_id) + '_' + str(time.time()) + '.xlsx'
    
    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    return response

# 請求書出力
def create_rental_invoice(rental_order_id):
    rental_order = RentalOrder.objects.get(pk=rental_order_id)
    company = rental_order.company
    print(company)

    # Excelのテンプレートファイルの読み込み
    wb = openpyxl.load_workbook('/django/main/static/tpl/RentalJpInvoice.xlsx')

    sheet = wb['請求書']

    sheet['K1'] = rental_order_id
    sheet['K2'] = datetime.date.today()

    sheet['L5'] = company.name
    sheet['L6'] = f"登録番号 {company.registration_number}"
    sheet['L7'] = f"〒 {str(company.zip)[0:3]}-{str(company.zip)[3:]}"
    sheet['L8'] = company.address
    sheet['L9'] = f"TEL : {company.tel}"
    sheet['L10'] = f"FAX : {company.fax}"

    client = rental_order.client

    sheet['C2'] = f"〒 {str(client.zip)[0:3]}-{str(client.zip)[3:]}"
    sheet['C3'] = f"{client.address}"
    sheet['C4'] = f"{client.name}　御中"
    sheet['C5'] = f"{client.office}　様"

    # 請求明細
    rental_order_rows =  RentalOrderRow.objects.filter(rental_order_id=rental_order_id)

    row=18
    for rental_order_row in rental_order_rows:
        # 出力対象のみ
        if rental_order_row.is_out == False:
            continue

        sheet['B'+str(row)] = rental_order_row.name
        sheet['G'+str(row)] = rental_order_row.count
        sheet['I'+str(row)] = rental_order_row.price
        sheet['J'+str(row)] = rental_order_row.count * rental_order_row.price
        sheet['K'+str(row)] = rental_order_row.memo
        row = row + 2
        
    # Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % str(rental_order_id) + '_' + str(time.time()) + '.xlsx'
    
    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    return response
