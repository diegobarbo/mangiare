from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


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


class FoodDetail(DetailView):
    model = Item
    template_name = 'dish/detail.html'


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dish:index')

    return render(request, 'dish/item-form.html', {'form': form})

# this is a class based view for create item


class CreateItem(CreateView):
    model = Item
    fields = ['nome', 'descricao', 'preco', 'image']
    template_name = 'dish/item-form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


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
