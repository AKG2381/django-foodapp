from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
# Create your views here.



def index(request):
    item_list = Item.objects.all()
    context = {"item_list": item_list,}
    return render(request,'food/index.html',context=context)

# def index(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('food/index.html')
#     context = {
#         "item_list": item_list,
#     }
#     return HttpResponse(template.render(context,request))


def items(request):
    return HttpResponse('<h1>This is an item View</h1>')


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {"item": item,}
    return render(request,'food/detail.html',context=context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item_form.html',{'form':form})

def update_item(request,item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item_form.html',{'form':form,'item':item})


def delete_item(request,item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item_delete.html',{'item':item})
    