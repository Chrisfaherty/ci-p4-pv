from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from pwmanagerapp.models import PwAccount
from pwmanagerapp.forms import CreateNewPwAccount
from django.contrib import messages

# Tech with Tim dejango course was used as insperation for the password manager
# This view is to save the password items to the database
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

# This view is create a new account instance and save it to the db
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

# This view is to edit the fields in a stored account
def edit(request, acc_id):
    acc = get_object_or_404(PwAccount, id=acc_id)
    if request.method == 'POST':
        form = CreateNewPwAccount(request.POST, instance=acc)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "You have updated your account details have been edited"
            )
            return redirect('view')
        else:
            messages.add_messages(
                request,
                messages.ERROR,
                "Whoops something is wrong!"
            )
    form = CreateNewPwAccount(instance=acc)
    context = {
        'form': form
    }
    return render(request, 'pwmanagerapp/edit_password.html', context)

# This view is to delete a stored account
def delete(request, acc_id):
    acc = get_object_or_404(PwAccount, id=acc_id)
    acc.delete()
    messages.add_message(
        request, messages.SUCCESS,
        "Your account has been deleted"
    )
    return redirect('view')

# this view is to render the stored account
def view(request):
    return render(request, "pwmanagerapp/viewpw.html", {})