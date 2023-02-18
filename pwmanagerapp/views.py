from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pwmanagerapp.models import ToDoList, Item
from pwmanagerapp.forms import CreateNewList

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
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
        return render(response, "pwmanagerapp/list.html", {"ls":ls})
    
    return render(response, "home.html", {})


def home(response):
    return render(response, 'pwmanagerapp/pwmanager.html', {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

            return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()

    return render(response, "pwmanagerapp/createpw.html", {"form":form})


def view(response):
    return render(response, "pwmanagerapp/viewpw.html", {})