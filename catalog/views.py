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
    room_form = RoomForm(prefix='room')
    category_form = CategoryForm(prefix='category')
    condition_form = ConditionForm(prefix='condition')
    item_form = ItemForm(prefix='item')


    #shows item list
    item_list = Item.objects.all()
    item_filter = ItemFilter(request.GET, queryset=item_list)
    if item_filter.is_valid():
        item_list = item_filter.qs

    paginator = Paginator(item_list, 20)  # Show 20 items per page.
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



def newview(request):
    room_form = RoomForm(request.POST, prefix='room')
    category_form = CategoryForm(request.POST, prefix='category')
    condition_form = ConditionForm(request.POST, prefix='condition')
    item_form = ItemForm(request.POST, prefix='item')
    if request.method == 'POST':
        if room_form.is_valid():
            room_form.save()
        if category_form.is_valid():
            category_form.save()
        if condition_form.is_valid():
            condition_form.save()
        if item_form.is_valid():
            item_form.save()
            print("this worked")
        return HttpResponseRedirect(request.path_info)
    else:
        return render(request, 'catalog/NewItem.html', {'room': room_form,
                                                        'category': category_form,
                                                        'condition': condition_form,
                                                        'item': item_form,
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


# -------------------- Category Views --------------------
class CategoryListView(ListView):
    model = Category

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'catalog/itemedit.html'
    # redirect_field_name = ''
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:category_list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catalog/deleteitem.html'
    success_url = reverse_lazy("catalog:category_list")


# -------------------- Condition Views --------------------
class ConditionListView(ListView):
    model = Condition


class ConditionUpdateView(UpdateView):
    model = Condition
    template_name = 'catalog/itemedit.html'
    form_class = ConditionForm
    success_url = reverse_lazy("catalog:condition_list")


class ConditionDeleteView(DeleteView):
    model = Condition
    template_name = 'catalog/deleteitem.html'
    success_url = reverse_lazy("catalog:condition_list")


# -------------------- Room Views --------------------
class RoomListView(ListView):
    model = Room


class RoomUpdateView(UpdateView):
    model = Room
    template_name = 'catalog/itemedit.html'
    # redirect_field_name = ''
    form_class = RoomForm
    success_url = reverse_lazy("catalog:room_list")


class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'catalog/deleteitem.html'
    success_url = reverse_lazy("catalog:room_list")


