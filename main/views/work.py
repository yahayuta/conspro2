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
from ..service import work_xls_handler

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
    return work_xls_handler.create_work_invoice(id)
