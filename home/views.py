from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    profile=Profile.objects.filter(user=request.user).first()
    expense =Expense.objects.filter(user=request.user)
    if request.method=='POST':
        text=request.POST.get("text")
        amount=request.POST.get("amount")
        expense_type=request.POST.get("expense_type")\
            
        expense=Expense (name=text,amount=amount,expense_type=expense_type,user=request.user) 
        expense.save()   
        if expense_type =='Postive':
            profile.balance+=float(amount)
        else:
            profile.expenses+=float(amount)
            profile.balance-=float(amount)
        profile.save()    
        return redirect('/')
    context ={'profile': profile}
    return render(request,"home.html",context) 