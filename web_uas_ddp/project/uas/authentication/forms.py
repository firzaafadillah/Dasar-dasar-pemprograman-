from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForms(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Perbaikan label untuk UX yang lebih baik
        self.fields['password1'].label = "Sandi Baru (Min. 8 Karakter)"
        self.fields['password2'].label = "Ulangi Sandi Baru"
        
class LoginForms(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Mengubah label field bawaan (username dan password)
        self.fields['username'].label = "Nama Pengguna atau Email"
        self.fields['password'].label = "Sandi Rahasia"
        
        # Menambahkan placeholder atau class CSS
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Masukkan Nama Pengguna',
            'class': 'form-control' # Untuk styling CSS
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Masukkan Sandi',
            'class': 'form-control'
        })   