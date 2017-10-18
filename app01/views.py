from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from app01 import models
import json

from app01.forms import UserForm

"""分页"""


from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger

class CustomPaginator(Paginator):
    def __init__(self,current_page,per_pager_num,*args,**kwargs):
        # per_pager_num  显示的页码数量
        self.current_page = int(current_page)
        self.per_pager_num = int(per_pager_num)
        super(CustomPaginator,self).__init__(*args,**kwargs)
    def pager_num_range(self):
        '''
        自定义显示页码数
        第一种：总页数小于显示的页码数
        第二种：总页数大于显示页数  根据当前页做判断  a 如果当前页大于显示页一半的时候  ，往右移一下
                                                b 如果当前页小于显示页的一半的时候，显示当前的页码数量
        第三种：当前页大于总页数
        :return:
        '''
        if self.num_pages < self.per_pager_num:
            return range(1,self.num_pages+1)
 
        half_part = int(self.per_pager_num/2)
        if self.current_page <= half_part:
            return range(1,self.per_pager_num+1)
 
        if (self.current_page+half_part) > self.num_pages:
            return range(self.num_pages-self.per_pager_num+1,self.num_pages)
        return range(self.current_page-half_part,self.current_page+half_part+1)
        
 
def users(request):
    user_list = models.UserInfo.objects.all()
    return render(request,'app01/users.html',{'user_list':user_list})
 
 
def add_user(request):
    if request.method == 'GET':
        obj = UserForm()
        return render(request,'app01/add_user.html',{'obj':obj})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect('/students/users/')
        else:
            return render(request,'app01/add_user.html',{'obj':obj})
 
 
def edit_user(request,nid):
    if request.method == "GET":
        data = models.UserInfo.objects.filter(id=nid).first()
        obj = UserForm({'username':data.username,'email':data.email})
        return render(request,'app01/edit_user.html',{'obj':obj,'nid':nid})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/students/users/')
        else:
            return render(request,'app01/edit_user.html',{'obj':obj,'nid':nid})
            



def students(request):
    cls_list = models.Classes.objects.all()
    stu_list = models.Student.objects.all()
    pagenum = 10
    paginator = Paginator(stu_list, pagenum) # 3 posts in each page
    page = request.GET.get('page')

    try:
        stu_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        stu_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        stu_list = paginator.page(paginator.num_pages)

    return render(request,'app01/students.html',{'stu_list':stu_list,'cls_list':cls_list,'page': page,'pagenum':pagenum})
    
    
 
def add_student(request):
    response = {'status':True,'message': None,'data':None}
    try:
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cls_id')
        obj = models.Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c
        )
        response['data'] = obj.id
    except Exception as e:
        response['status'] = False
        response['message'] = '用户输入错误'
 
    result = json.dumps(response,ensure_ascii=False)
    return HttpResponse(result)
 
def del_student(request):
    ret = {'status': True}
    try:
        nid = request.GET.get('nid')
        models.Student.objects.filter(id=nid).delete()
    except Exception as e:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))
 
def edit_student(request):
    response = {'code':1000, 'message': None}
    try:
        nid = request.POST.get('nid')
        user = request.POST.get('user')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cls_id = request.POST.get('cls_id')
        models.Student.objects.filter(id=nid).update(
            username=user,
            age=age,
            gender=gender,
            cs_id=cls_id
        )
    except Exception as e:
        response['code'] = 1001
        response['message'] = str(e)
    return HttpResponse(json.dumps(response))
 
 
def test_ajax_list(request):
    print(request.POST.getlist('k'))
    return HttpResponse('...')