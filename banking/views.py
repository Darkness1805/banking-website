
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from gg.models import*



def loginn(request):
    nn = bank.objects.all()
    data = {
        'nn':nn,
    }
    
    return render(request,"index.html",data)


def CREAT_USER(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Account_no= request.POST.get('Account_no')
        Balance = request.POST.get('Balance')
        Amount = request.POST.get('Amount')

        nn = bank(
            Name = Name,
            Account_no = Account_no,
            Balance = Balance,
        )
        nn.save()

    return redirect('home')
    return render(request,"home")


def Edit(request):
    nn= bank.objects.all
    data = {
        'nn':nn
    }
    return redirect(request,'index.html',data)

def deposit(request,id):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Account_no= request.POST.get('Account_no')
        Balance = request.POST.get('Balance')
        amount = request.POST.get('Amount')
        ll = int(Balance)+ int(amount)
        Balance = ll
        nn = bank(
            id = id,
             Name = Name,
            Account_no = Account_no,
            Balance = Balance,
            amount = amount,
        )
        nn.save()
        return redirect('home')

    return redirect(request,'index.html')

def Withdraw(request,id):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Account_no= request.POST.get('Account_no')
        Balance = request.POST.get('Balance')
        amount = request.POST.get('Amount')
        ll = int(Balance)- int(amount)
        Balance = ll
        nn = bank(
            id = id,
             Name = Name,
            Account_no = Account_no,
            Balance = Balance,
            amount = amount,
        )
        nn.save()
        return redirect('home')

    return redirect(request,'index.html')