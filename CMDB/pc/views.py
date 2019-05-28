from django.shortcuts import render

from .forms import ServicePcTypeForm
from .models import ServicePcType
from .models import SystemType
from .forms import SystemTypeForm
from django.shortcuts import redirect, reverse
from .forms import OperForm
from .models import Oper
from .models import Pc
from .forms import PcForm
from django.http import HttpResponse

# Create your views here.


############
def edit_pc(request) :
    pc_id = request.GET.get('pc_id')
    if pc_id is None :
        return HttpResponse('404')
    pc = Pc.objects.get(id=pc_id)
    if pc is None :
        return HttpResponse('404')

    if request.method == 'POST' :
        form = PcForm(request.POST)
        if form.is_valid() :
            name = form.cleaned_data.get('name')
            ddr = form.cleaned_data.get('ddr')
            disk = form.cleaned_data.get('disk')
            ssd = form.cleaned_data.get('ssd')
            cpu = form.cleaned_data.get('cpu')
            productor = form.cleaned_data.get('productor')
            ip = form.cleaned_data.get('ip')
            mac = form.cleaned_data.get('mac')

            systemtype = form.cleaned_data.get('systemtype')
            servicetype = form.cleaned_data.get('servicetype')
            oper = form.cleaned_data.get('oper')

            Pc.objects.filter(id=pc_id).update(name=name,
                 ddr=ddr,
                 disk=disk,
                 ssd=ssd,
                 cpu=cpu,
                 productor=productor,
                 ip=ip,
                 mac=mac,
                 systemtype_id=systemtype,
                 servicetype_id=servicetype,
                 oper_id=oper)
            return redirect(reverse('pc_pcs'))
        stypes = ServicePcType.objects.all()
        systypes = SystemType.objects.all()
        os = Oper.objects.all()

        return render(request, 'pc/add_pc.html',
                      {'form':form,
                       'stypes':stypes,
                       'systypes':systypes,
                       'os':os, 'pc_active':'active'})

    else :
        form = PcForm()
        stypes = ServicePcType.objects.all()
        systypes = SystemType.objects.all()
        os = Oper.objects.all()
        return render(request, 'pc/edit_pc.html',
                      {'form':form,
                       'pc':pc,
                       'stypes':stypes,
                       'systypes':systypes,
                       'os':os, 'pc_active':'active'})
#############


from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

def index(request) :
    return render(request, 'base.html')
##########################################

def pcs(request) :
    ps = Pc.objects.all()
    return render(request, 'pc/pcs.html', {'sts':ps, 'pc_active':'active'})

def add_pc(request) :
    if request.method == 'POST' :
        form = PcForm(request.POST)
        if form.is_valid() :
            name = form.cleaned_data.get('name')
            ddr = form.cleaned_data.get('ddr')
            disk = form.cleaned_data.get('disk')
            ssd = form.cleaned_data.get('ssd')
            cpu = form.cleaned_data.get('cpu')
            productor = form.cleaned_data.get('productor')
            ip = form.cleaned_data.get('ip')
            mac = form.cleaned_data.get('mac')

            systemtype = form.cleaned_data.get('systemtype')
            servicetype = form.cleaned_data.get('servicetype')
            oper = form.cleaned_data.get('oper')

            Pc(name=name,
                 ddr=ddr,
                 disk=disk,
                 ssd=ssd,
                 cpu=cpu,
                 productor=productor,
                 ip=ip,
                 mac=mac,
                 systemtype_id=systemtype,
                 servicetype_id=servicetype,
                 oper_id=oper).save()
            return redirect(reverse('pc_pcs'))
        stypes = ServicePcType.objects.all()
        systypes = SystemType.objects.all()
        os = Oper.objects.all()

        return render(request, 'pc/add_pc.html',
                      {'form':form,
                       'stypes':stypes,
                       'systypes':systypes,
                       'os':os, 'pc_active':'active'})

    else :
        form = PcForm()
        stypes = ServicePcType.objects.all()
        systypes = SystemType.objects.all()
        os = Oper.objects.all()
        return render(request, 'pc/add_pc.html',
                      {'form':form,
                       'stypes':stypes,
                       'systypes':systypes,
                       'os':os, 'pc_active':'active'})

##################################

def opers(request) :
    os = Oper.objects.all()
    return render(request, 'pc/opers.html', {'sts':os, 'oper_active':'active'})

def add_oper(request) :
    if request.method == 'POST' :
        form = OperForm(request.POST)
        if form.is_valid() :
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            email = form.cleaned_data.get('email')
            telephone = form.cleaned_data.get('telephone')
            sex = form.cleaned_data.get('sex')
            if sex == '1' :
                sex = True
            else :
                sex = False
            Oper(name=name, age=age, email=email, telephone=telephone, sex=sex).save()
            return redirect(reverse('pc_opers'))
        info = {
            'name':form.cleaned_data.get('name'),
            'age': form.cleaned_data.get('age'),
            'email': form.cleaned_data.get('email'),
            'telephone': form.cleaned_data.get('telephone'),
        }
        return render(request, 'pc/add_oper.html', {'form':form, 'info':info, 'oper_active':'active'})

    else :
        form = OperForm()
        return render(request, 'pc/add_oper.html', {'form':form, 'oper_active':'active'})




def system_types(request) :
    sts = SystemType.objects.all()
    return render(request, 'pc/system_types.html', {'sts':sts, 'system_active':'active'})

def add_system_type(request) :
    if request.method == 'POST' :
        form = SystemTypeForm(request.POST)
        if form.is_valid() :
            name = form.cleaned_data.get('name')
            productor = form.cleaned_data.get('productor')
            SystemType(name=name, productor=productor).save()
            return redirect(reverse('pc_system_types'))
    else :
        form = SystemTypeForm()
        return render(request, 'pc/add_system_type.html', {'form':form, 'system_active':'active'})

def service_types(request) :
    sts = ServicePcType.objects.all()
    return render(request, 'pc/service_types.html', {'sts':sts, 'service_active':'active'})

def add_service_type(request) :
    if request.method == 'POST' :
        form = ServicePcTypeForm(request.POST)
        if form.is_valid() :
            name = form.cleaned_data.get('name')
            addr = form.cleaned_data.get('addr')
            ServicePcType(name=name, addr=addr).save()
            return redirect(reverse('pc_service_types'))
    else :
        form = ServicePcTypeForm()
        return render(request, 'pc/add_service_type.html', {'form':form, 'service_active':'active'})
