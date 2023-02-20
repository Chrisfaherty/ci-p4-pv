from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from pwmanagerapp.models import ToDoList
from pwmanagerapp.forms import CreateNewList

def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if ls in request.user.todolist.all():

        if request.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()
            elif response.Post.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
        return render(request, "pwmanagerapp/list.html", {"ls":ls})
    
    return render(request, "home.html", {})


#def home(request):
    #return render(request, 'pwmanagerapp/pwmanager.html', {})


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        

        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.user = request.user
            save_form.save()

            return redirect('view')
    else:
        form = CreateNewList()

    return render(request, "pwmanagerapp/createpw.html", {"form":form})


def edit(request, ls_id):
    ls = get_object_or_404(ToDoList, id=ls_id)
    if request.method == 'POST':
        form = CreateNewList(request.POST, instance=ls)
        if form.is_valid():
            form.save()
            return redirect('view')
    form = CreateNewList(instance=ls)
    context = {
        'form': form
    }
    return render(request, 'pwmanagerapp/edit_password.html', context)


def delete(request, ls_id):
    ls = get_object_or_404(ToDoList, id=ls_id)
    ls.delete()
    return redirect('view')


def view(request):
    return render(request, "pwmanagerapp/viewpw.html", {})