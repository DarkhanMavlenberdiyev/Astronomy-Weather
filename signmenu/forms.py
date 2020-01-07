from .models import User,DeleteUser
from django.forms import ModelForm, TextInput,PasswordInput


class UserForm(ModelForm):
	class Meta:
		model= User
		fields = ['user_name','password']
		widgets = {'user_name':TextInput(attrs={'class':'form-control','name':'user_name','id':'user_name','placeholder':'Введите ваш логин'}),
		'password':PasswordInput(attrs={'class':'form-control','name':'password','id':'password','placeholder':'Введите пароль'})}
		

class DeleteUserForm(ModelForm):
	class Meta:
		model= DeleteUser
		fields = ['user_name','password']
		widgets = {'user_name':TextInput(attrs={'class':'form-control','name':'user_name','id':'user_name','placeholder':'Введите ваш логин'}),
		'password':PasswordInput(attrs={'class':'form-control','name':'password','id':'password','placeholder':'Введите пароль'})}
		