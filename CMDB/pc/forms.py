from django import forms
import re
from .models import ServicePcType, Oper, SystemType

class ServicePcTypeForm(forms.Form) :
    name = forms.CharField(max_length=32)
    addr = forms.CharField(max_length=32)

class SystemTypeForm(forms.Form) :
    name = forms.CharField(max_length=64)
    productor = forms.CharField(max_length=64)

class OperForm(forms.Form) :
    def is_telephone(value):
        mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17 [678]|18[0-9]|14[57])[0-9]{8}$')
        if not mobile_re.match(value):
            raise forms.ValidationError('手机号有误')
    name = forms.CharField(max_length=32)
    age = forms.IntegerField(initial=35)
    email = forms.EmailField(max_length=64)
    telephone = forms.CharField(max_length=32, validators=[is_telephone])
    sex = forms.ChoiceField(
        widget=forms.Select(),
        choices=((1, '男'), (2, '女')),
        initial=(2, '女')
    )


class PcForm(forms.Form) :
    name = forms.CharField(max_length=32)

    ddr = forms.IntegerField(initial=4)
    disk = forms.IntegerField(initial=320)
    ssd = forms.IntegerField(initial=128)
    cpu = forms.CharField(max_length=32)
    productor = forms.CharField(max_length=32)

    mac = forms.CharField(max_length=32)
    ip = forms.CharField(max_length=128)

    systemtype = forms.ChoiceField(
        widget=forms.Select(),
        choices=((o.id, o.name) for o in SystemType.objects.all()),
        initial=(1, '未知操作系统')
    )
    servicetype = forms.ChoiceField(
        widget=forms.Select(),
        choices=((o.id, o.name) for o in ServicePcType.objects.all()),
        initial=(1, '未知服务器类型')
    )
    oper = forms.ChoiceField(
        widget=forms.Select(),
        choices=((o.id, o.name) for o in Oper.objects.all()),
        initial=(1, 'CTO')
    )

