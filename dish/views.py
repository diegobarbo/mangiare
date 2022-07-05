from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView


def index(request):
    item_list = Item.objects.all()    
    context = {'item_list': item_list,}
    return render(request, 'dish/index.html', context)


class IndexClassView(ListView):
    model = Item
    template_name = 'dish/index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse('isso é uma view')

def detail(request, id):
    item_detail = Item.objects.get(pk=id)
    context = {'item_detail': item_detail,}
    return render(request, 'dish/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dish:index')

    return render(request, 'dish/item-form.html', {'form': form})

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('dish:index')
    
    return render(request, 'dish/item-form.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('dish:index')

    return render(request, 'dish/item-delete.html', {'item': item})
