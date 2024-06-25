from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django_filters.views import FilterView
from django.urls import reverse_lazy

from ..models import Inventory, Work
from ..filters import InventoryFilter
from ..service import inventory_xls_handler
from ..forms import InventoryEditForm, InventoryOrderRowFormset

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
@login_required
def inventory_new(request):
    form = InventoryEditForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        work = form.save(commit=False)
        formset = InventoryOrderRowFormset(request.POST, instance=work)
        if formset.is_valid():
            work.save()
            formset.save()
            return redirect('inventory_list')
        else:
            context['formset'] = formset
    else:
        context['formset'] = InventoryOrderRowFormset()

    return render(request, 'inventory_edit.html', context)

# 更新
@login_required
def inventory_edit(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    form = InventoryEditForm(request.POST or None, instance=inventory)
    formset = InventoryOrderRowFormset(request.POST or None, instance=inventory)
    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return redirect('inventory_list')

    # 作業履歴を取得する
    works = Work.objects.filter(work_inventory_id=pk)

    print(works)

    context = {
        'form': form,
        'formset': formset,
        'works': works
    }

    return render(request, 'inventory_edit.html', context)

# 削除
class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'inventory_edit.html'
    model = Inventory
    success_url = reverse_lazy('inventory_list')

# 発注書出力
@login_required
def download_ordersheet(request, id):
    return inventory_xls_handler.create_ordersheet(id)

# 請求書出力
@login_required
def download_jpinvoice(request, id):
    return inventory_xls_handler.create_jpinvoice(id)

# Proforma Invoice出力
@login_required
def download_proforma_invoice(request, id):
    return inventory_xls_handler.create_proforma_invoice(id)
