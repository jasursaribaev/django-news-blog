from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def clean_password_2(self):
        data = self.cleaned_data
        if data['password'] != data['password_2']:
            raise forms.ValidationError('Parolingiz bir biriga teng emas!')
        return data['password_2']
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'image']