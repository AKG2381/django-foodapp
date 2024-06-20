from django.forms.models import BaseModelForm
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic import ListView ,DetailView ,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context = "item_list"

# def index(request):
#     item_list = Item.objects.all()
#     context = {"item_list": item_list,}
#     return render(request,'food/index.html',context=context)

# def index(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('food/index.html')
#     context = {
#         "item_list": item_list,
#     }
#     return HttpResponse(template.render(context,request))


def items(request):
    return HttpResponse('<h1>This is an item View</h1>')


# def detail(request,item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {"item": item,}
#     return render(request,'food/detail.html',context=context)

class FoodDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'

# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request,'food/item_form.html',{'form':form})
    
class ItemCreateView(LoginRequiredMixin,CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item_form.html'
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user_name = self.request.user
        return super().form_valid(form)

@login_required
def update_item(request,item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item_form.html',{'form':form,'item':item})

@login_required
def delete_item(request,item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item_delete.html',{'item':item})
    