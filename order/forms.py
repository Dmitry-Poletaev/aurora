from django import forms
from .models import Order
from captcha.fields import CaptchaField


class OrderForm(forms.ModelForm):
    name = forms.CharField(label='Имя',max_length=30)
    last_name = forms.CharField(label='Фамилия',max_length=40, required=False)
    shipping_address = forms.CharField(label='Адрес',required=False)
    phone =  forms.CharField(label='Телефон',max_length=30,required=False)
    email = forms.EmailField(label='E-mail',max_length=40)
    comment = forms.CharField(label='Комментарий к заказу',widget=forms.Textarea(),max_length=300)
    captcha = CaptchaField(label='Введите текст с картинки',
            error_messages={'invalid':'Неправильный текст'})

    class Meta:
        model = Order
        fields  = ('name','last_name','shipping_address',
        'phone','email','comment','captcha')
