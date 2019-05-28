from django.db import models
from datetime import datetime

# Create your models here.


class ServicePcType(models.Model) :
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    ct = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create_default_service_pc_type():
        s = ServicePcType(name='未知服务器类型')
        s.addr = '火星'
        s.save()

class SystemType(models.Model) :
    name = models.CharField(max_length=64)
    productor = models.CharField(max_length=64)
    ct = models.DateTimeField(auto_now_add=True)


    @staticmethod
    def create_default_system_type():
        s = SystemType(name='未知操作系统类型')
        s.productor = '外星人'
        s.save()

class Oper(models.Model) :
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=35)
    email = models.EmailField(max_length=64)
    telephone = models.CharField(max_length=32)
    sex = models.BooleanField(default=False)

    ct = models.DateTimeField(auto_now_add=True)


    @staticmethod
    def create_default_oper():
        o = Oper(name='cto', age='60', email='root@embsky.com', telephone='110', sex=True)


class Pc(models.Model) :
    name = models.CharField(max_length=32)

    ddr = models.IntegerField(default=4)
    disk = models.IntegerField(default=320)
    ssd = models.IntegerField(default=128)
    cpu = models.CharField(max_length=32)
    productor = models.CharField(max_length=32)

    mac = models.CharField(max_length=32)
    ip = models.CharField(max_length=128)

    ct = models.DateTimeField(auto_now_add=True)

    systemtype = models.ForeignKey(SystemType, default=1, related_name='pcs', on_delete=models.SET_DEFAULT)
    servicetype = models.ForeignKey(ServicePcType, default=1, related_name='pcs', on_delete=models.SET_DEFAULT)
    oper = models.ForeignKey(Oper, default=1, related_name='pcs', on_delete=models.SET_DEFAULT)
