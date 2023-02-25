from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from pwmanagerapp.models import PwAccount
from pwmanagerapp.forms import CreateNewPwAccount

def index(request, id):
    acc = PwAccount.objects.get(id=id)

    if acc in request.user.pwaccount.all():

        if request.method == "POST":
            if response.POST.get("save"):
                for item in acc.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()
            elif response.Post.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    acc.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
        return render(request, "pwmanagerapp/list.html", {"acc":acc})
    
    return render(request, "home.html", {})


#def home(request):
    #return render(request, 'pwmanagerapp/pwmanager.html', {})


def create(request):
    if request.method == "POST":
        form = CreateNewPwAccount(request.POST)
        

        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.user = request.user
            save_form.save()

            return redirect('view')
    else:
        form = CreateNewPwAccount()

    return render(request, "pwmanagerapp/createpw.html", {"form":form})


def edit(request, acc_id):
    acc = get_object_or_404(PwAccount, id=acc_id)
    if request.method == 'POST':
        form = CreateNewPwAccount(request.POST, instance=acc)
        if form.is_valid():
            form.save()
            return redirect('view')
    form = CreateNewPwAccount(instance=acc)
    context = {
        'form': form
    }
    return render(request, 'pwmanagerapp/edit_password.html', context)


def delete(request, acc_id):
    acc = get_object_or_404(PwAccount, id=acc_id)
    acc.delete()
    return redirect('view')


def view(request):
    return render(request, "pwmanagerapp/viewpw.html", {})