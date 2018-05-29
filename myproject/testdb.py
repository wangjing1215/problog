# -*- coding: utf-8 -*-

from django.http import HttpResponse

from testmodel.models import Citys


# 数据库操作
def adddata(request):
    filepath=r'/Users/yons/wj/prowork/myproject/myproject/date/china-regions/data/json/cities.json'
    with open(filepath, "r") as f:
        temp = f.readlines()
    oldid=''
    partlist=[]
    alllist=[]
    for i in temp:
        if i.find('[') > 0:
            id=i[i.find('"')+1:i.rfind('"')]
            oldid=id
        if i.find('code') > 0:
            code=i[i.find('"code": "')+9:i.rfind('"')]
            partlist.append(code)
        if i.find('name') > 0:
            name = i[i.find('"name": "') + 9:i.rfind('"')]
            partlist.append(name)
        if i.find('province') > 0:
            province = i[i.find('"province": "') + 13:i.rfind('"')]
            partlist.append(province)
        if i.find('{') > 0:
            partlist.append(oldid)
        if i.find('}') > 0:
            alllist.append(partlist)
            partlist=[]
    ppid=111000
    for j in alllist:
        test = Citys()
        test.addid=str(ppid)
        test.oid = j[0]
        test.code = j[1]
        test.name = j[2]
        test.province_code = j[3]
        test.save()
        ppid=ppid+1
    return HttpResponse("<p>数据添加成功！</p>")
def testdb(request):
    response = ""

    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Citys.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Citys.objects.filter(id=1)

    # 获取单个对象
    response3 = Citys.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    #Citys.objects.order_by('name')[0:2]

    # 数据排序
    #Citys.objects.order_by("id")

    # 上面的方法可以连锁使用
    #Citys.objects.filter(name="runoob").order_by("id")

    # 输出所有数据

    for var in list:
        temp=''
        oid=str(var.id)
        id=str(var.oid)
        code=str(var.code)
        name=var.name
        #name=name.decode('utf-8')
        province_code=var.province_code
        #province_code = province_code.decode('utf-8')
        temp='<br>'+'{'+'id:'+id+' '+'code:'+code+' '+'name:'+name+' '+'province_code:'+ province_code+'}'+'<br/>'
        response1 += temp
    response = response1
    return HttpResponse("<p>" + response + "</p>")