from django.shortcuts import render,redirect,HttpResponse
from .models import *

def index(request):
    recipe=Recipe.objects.all()
    context={
        "recipe":recipe
    }
    
    return render(request,'home.html',context)

def create(request):
    user_id=request.user.id
    user=User.objects.get(pk=user_id)
    categories=RecipeCategory.objects.all()
    context={
        "categories":categories,
    }
    
    if request.method=="POST":
        title=request.POST.get('title')
        category_id=request.POST.get('category_id')
        procedure=request.POST.get('procedure')
        ingredients=request.POST.get('ingredients')
        picture=request.FILES.get('picture')
        
        category=RecipeCategory.objects.get(pk=category_id)
        
        Recipe.objects.create(
            title=title,
            category=category,
            picture=picture,
            ingredients=ingredients,
            procedure=procedure,
            user=user
            
        )
        return redirect('/')
    return render(request,'create.html',context)


def view_recipe(request,pk):
    
    recipe=Recipe.objects.get(pk=pk)
    
    user=User.objects.get(pk=recipe.user_id)
    show=True
    if  request.user.is_authenticated and request.user.id==recipe.user_id:
        context={
            "recipe":recipe,
            "user":user,
            "show":show,
        }
        return render(request,'view_recipe.html',context)
    else:
        context={
                "recipe":recipe,
            "user":user,
        }
        
        return render(request,'view_recipe.html',context)

def edit(request,pk):
    recipe=Recipe.objects.get(pk=pk)
    categories=RecipeCategory.objects.all()
    context={
            "recipe":recipe,
            "categories":categories,
            
        }
    if request.method=="POST":
        recipe.title=request.POST.get('title')
        recipe.category_id=request.POST.get('category_id')
        recipe.procedure=request.POST.get('procedure')
        recipe.ingredients=request.POST.get('ingredients')
        #recipe.picture=request.FILES.get('picture')
        recipe.save()
        return redirect('/')
    return render(request,'edit.html',context) 


def delete(request,pk):
    recipe=Recipe.objects.get(pk=pk) 
    recipe.delete()
    return redirect("/")
    
    
def category(request):
    categories=RecipeCategory.objects.all()
    context={
        "categories":categories,
    }
    return render(request,'category.html',context)
   
    
def category_recipe(request,pk):
    recipe=Recipe.objects.all().filter(category_id=pk)
    
    context={
        "recipe":recipe,
    }
    
    return render(request,'home.html',context)


def create_category(request):
    name=request.POST.get('name')
    
    if request.method=="POST":
        RecipeCategory.objects.create(name=name)
        return redirect('/')
   
    return render(request,'create_category.html')
