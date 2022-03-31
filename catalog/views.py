from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .models import *
from .forms import *
from .filters import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


# @api_view(['GET'])
def mainview(request):
    if request.method == 'POST':
        room_form = RoomForm(request.POST, prefix='room')
        category_form = CategoryForm(request.POST, prefix='category')
        condition_form = ConditionForm(request.POST, prefix='condition')
        item_form = ItemForm(request.POST, prefix='item')

        if room_form.is_valid():
            room_form.save()
        if category_form.is_valid():
            category_form.save()
        if condition_form.is_valid():
            condition_form.save()
        if item_form.is_valid():
            item_form.save()
            print("this worked")
        return HttpResponseRedirect('/')
    else:
        # generate forms
        room_form = RoomForm(prefix='room')
        category_form = CategoryForm(prefix='category')
        condition_form = ConditionForm(prefix='condition')
        item_form = ItemForm(prefix='item')


        #shows item list
        item_list = Item.objects.all()
        item_filter = ItemFilter(request.GET, queryset=item_list)
        if item_filter.is_valid():
            item_list = item_filter.qs

        paginator = Paginator(item_list, 20)  # Show 25 contacts per page.
        page_number = request.GET.get('page', 1)
        try:
            page_obj = paginator.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = paginator.page(paginator.num_pages)

    return render(request, 'catalog/main.html', {'room': room_form,
                                                 'category': category_form,
                                                 'condition': condition_form,
                                                 'item': item_form,
                                                 'item_list': item_list,
                                                 'filter': item_filter,
                                                 'page_obj': page_obj,
                                                 })


class HomeView(TemplateView):
    template_name = 'catalog/MAIN.html'


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'catalog/itemedit.html'
    # redirect_field_name = ''
    form_class = ItemForm
    success_url = reverse_lazy("catalog:main")


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'catalog/deleteitem.html'
    success_url = reverse_lazy("catalog:main")


