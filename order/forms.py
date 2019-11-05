from django import forms
from .models import Order
from captcha.fields import CaptchaField


class OrderForm(forms.ModelForm):
    name = forms.CharField(label='Имя',max_length=30)
    shipping_address = forms.CharField(label='Адрес',required=False)
    city =  forms.CharField(label='Город',max_length=100,required=False)
    phone =  forms.CharField(label='Телефон',max_length=30,required=False)
    email = forms.EmailField(label='E-mail',max_length=40)
    captcha = CaptchaField(label='Введите текст с картинки',
            error_messages={'invalid':'Неправильный текст'})

    class Meta:
        model = Order
        fields  = ('name','shipping_address','city',
        'phone','email','captcha')
