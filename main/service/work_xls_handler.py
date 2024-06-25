import openpyxl
import datetime
import time

from django.http import HttpResponse
from ..models import Work, WorkRow

# 作業帳票出力
def create_work_invoice(id):
    #id = request.GET['id']
    print(id)

    work = Work.objects.get(pk=id)
    company = work.company
    print(company)

    # Excelのテンプレートファイルの読み込み
    wb = openpyxl.load_workbook('/django/main/static/tpl/WorkInvoice.xlsx')

    sheet = wb['見積書']
    sheet['K1'] = id
    sheet['K2'] = datetime.date.today()

    sheet['L6'] = company.name
    sheet['L7'] = "〒 " + str(company.zip)[0:3] + '-' + str(company.zip)[3:]
    sheet['L8'] = company.address
    sheet['L9'] = company.tel
    sheet['L10'] = company.fax

    client = work.client

    sheet['C2'] = "〒 " + str(client.zip)[0:3] + '-' + str(client.zip)[3:]
    sheet['C3'] = client.address
    sheet['C4'] = client.name + " 御中"
    sheet['C5'] = client.office

    # 作業明細
    work_rows =  WorkRow.objects.filter(work_id=id)

    row=18
    for work_row in work_rows:
        # 出力対象のみ
        if work_row.is_out == False:
            continue

        sheet['B'+str(row)] =  f'{work.work_inventory.name},{work.work_inventory.serial_no}'
        sheet['B'+str(row+1)] = work_row.name
        sheet['G'+str(row)] = work_row.count
        sheet['H'+str(row)] = work_row.price
        row = row + 2

    sheet_invoice = wb['請求書']
    sheet_invoice['L6'] = '登録番号 ' + str(company.registration_number)

    sheet_order = wb['オーダー表']
    sheet_order['C4'] = client.name
    sheet_order['C5'] = f'{work.work_inventory.name},{work.work_inventory.serial_no}'
    sheet_order['C7'] = work.name
    row=18

    for work_row in work_rows:
        # 部品以外は記載しない
        if work_row.type != '2':
            continue
        
        # 出力対象のみ
        if work_row.is_out == False:
            continue

        sheet_order['B'+str(row)] = work_row.parts_name
        sheet_order['B'+str(row+1)] = work_row.name
        sheet_order['F'+str(row)] = work_row.count
        sheet_order['G'+str(row)] = work_row.price
        sheet_order['I'+str(row)] = work_row.parts_delivery_date
        
        if work_row.client:
            sheet_order['J'+str(row)] = work_row.client.name

        row = row + 2

    # Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % f'{work.work_inventory.name}_{work.work_inventory.serial_no}' + '_' + str(time.time()) + '.xlsx'

    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    # 生成したHttpResponseをreturnする
    return response