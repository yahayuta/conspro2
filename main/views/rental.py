from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django_filters.views import FilterView

from ..models import RentalOrder
from ..filters import RentalOrderFilter
from ..forms import RentalOrderCreateForm, RentalOrderRowFormset
from ..service import rental_xls_handler

# 検索一覧画面
class RentalOrderFilterView(LoginRequiredMixin, FilterView):
    model = RentalOrder
    filterset_class = RentalOrderFilter
    queryset = RentalOrder.objects.all().order_by('-created')
    strict = False
    paginate_by = 5
    template_name = 'rental_order_list.html'

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
class RentalOrderListView(LoginRequiredMixin, ListView):
    model = RentalOrder
    template_name = 'rental_order_list.html'
    paginate_by = 5

@login_required
def rental_order_new(request):
    form = RentalOrderCreateForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        rental_order = form.save(commit=False)
        formset = RentalOrderRowFormset(request.POST, instance=rental_order)
        if formset.is_valid():
            rental_order.save()
            formset.save()
            return redirect('rental_order_list')
        else:
            context['formset'] = formset
    else:
        context['formset'] = RentalOrderRowFormset()

    return render(request, 'rental_order_edit.html', context)

@login_required
def rental_order_edit(request, pk):
    rental_order = get_object_or_404(RentalOrder, pk=pk)
    form = RentalOrderCreateForm(request.POST or None, instance=rental_order)
    formset = RentalOrderRowFormset(request.POST or None, instance=rental_order)
    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return redirect('rental_order_list')

    context = {
        'form': form,
        'formset': formset
    }

    return render(request, 'rental_order_edit.html', context)

# 出庫返却伝票出力
@login_required
def download_rental_ordersheet(request, id):
    return rental_xls_handler.create_rental_ordersheet(id)
