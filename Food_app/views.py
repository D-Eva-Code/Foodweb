from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import Itemform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView 

# Create your views here.
def menu(request):
    food = Item.objects.all()
    return HttpResponse(food)

@login_required
def item(request):
    # template = loader.get_template("index.html")
    list = Item.objects.all()
    # return HttpResponse(template.render(context,request))
    return render (request, "item.html", {"list":list} )

# @login_required
# def details(request,item_id):
#     list = Item.objects.get(pk = item_id)
#     return render(request, "detail.html", {"list":list})

class ModelDetailView(DetailView): # using a class based view to write the detail view
    model = Item
    template_name = "detail.html"
    context_object_name = "list"


@login_required
def create(request):
    if request.method == "POST":
      form= Itemform(request.POST)
      if form.is_valid():
        form.save()
        messages.success(request, "item added successfully")
        return redirect('item')
    else:
        form = Itemform()
    return render(request, "forms.html", {"form": form})

@login_required
def edit(request,edit_id):
    edit = Item.objects.get(pk = edit_id)
    if request.method =="POST":
        
        new_edit= Itemform(request.POST, instance= edit)
        if new_edit.is_valid():
            new_edit.save()
            messages.success(request, "Item edited successfully")
            return redirect("item")
        
    else:
        new_edit= Itemform(instance= edit)
        return render(request, "edit.html", {"new_edit": new_edit})

@login_required
def delete(request,delete_id):
    delete = Item.objects.get(pk = delete_id)
    if request.method =="POST":
        delete.delete()
        messages.success(request, "Item deleted successfully")
        return redirect("item")
       
      
    return render(request, "delete.html", {"delete": delete})
    
        
