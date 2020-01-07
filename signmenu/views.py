from django.shortcuts import render
from .forms import UserForm,DeleteUserForm
from .models import User, DeleteUser
from django.http import HttpResponseRedirect

def sign(request):


	if (request.method=='POST'):
		form = UserForm(request.POST)
		form.save()

	form = UserForm()



	context = {'form':form}


	return render(request,'signmenu/sign.html',context)


def signin(request):


	if (request.method=='POST'):
		form = DeleteUserForm(request.POST)
		
       	
		
		for user in User.objects.all():
			if user.user_name == form['user_name'].value() and user.password == form['password'].value():
				user.delete()

	form = DeleteUserForm()


	context = {"form":form}


	

	
	return render(request,'signmenu/signin.html',context)

