import openpyxl
import time
import datetime

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Work, WorkRow
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import WorkCreateForm, WorkRowFormset
from django.shortcuts import render, redirect, get_object_or_404

from django_filters.views import FilterView
from ..filters import WorkFilter

# 検索一覧画面
class WorkFilterView(LoginRequiredMixin, FilterView):
    model = Work
    filterset_class = WorkFilter
    queryset = Work.objects.all().order_by('-created')
    strict = False
    paginate_by = 5
    template_name = 'work_list.html'

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
class WorkListView(LoginRequiredMixin, ListView):
    model = Work
    template_name = 'work_list.html'
    paginate_by = 5

@login_required
def work_new(request):
    form = WorkCreateForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        work = form.save(commit=False)
        formset = WorkRowFormset(request.POST, instance=work)
        if formset.is_valid():
            work.save()
            formset.save()
            return redirect('work_list')
        else:
            context['formset'] = formset
    else:
        context['formset'] = WorkRowFormset()

    return render(request, 'work_edit.html', context)

@login_required
def work_edit(request, pk):
    work = get_object_or_404(Work, pk=pk)
    form = WorkCreateForm(request.POST or None, instance=work)
    formset = WorkRowFormset(request.POST or None, instance=work)
    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return redirect('work_list')

    context = {
        'form': form,
        'formset': formset
    }

    return render(request, 'work_edit.html', context)

@login_required
def download_invoice(request, id):
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
        sheet['B'+str(row)] =  f'{work.machine_name},{work.serial_no}'
        sheet['B'+str(row+1)] = work_row.name
        sheet['G'+str(row)] = work_row.count
        sheet['H'+str(row)] = work_row.price
        row = row + 2

    sheet_invoice = wb['請求書']
    sheet_invoice['L6'] = '登録番号 ' + str(company.registration_number)

    sheet_order = wb['オーダー表']
    sheet_order['C4'] = client.name
    sheet_order['C5'] = work.serial_no
    sheet_order['C7'] = work.name
    row=18
    for work_row in work_rows:
        # 部品以外は記載しない
        if work_row.type != '2':
            continue

        sheet_order['B'+str(row)] = work_row.parts_name
        sheet_order['B'+str(row+1)] = work_row.name
        sheet_order['F'+str(row)] = work_row.count
        sheet_order['G'+str(row)] = work_row.price
        sheet_order['I'+str(row)] = work_row.parts_delivery_date
        sheet_order['J'+str(row)] = work_row.client.name

        row = row + 2

    # Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % work.machine_name + '_' + str(time.time()) + '.xlsx'

    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    # 生成したHttpResponseをreturnする
    return response