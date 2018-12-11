from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
import  uuid
import os
import json
# Create your views here.
def file_1(request):
    '''
    文件上传预览
    :param request:
    :return:
    '''
    if request.method=='GET':
        return render(request,'file_upload.html')
    filename =request.FILES.get('customer_excel')
    with open(filename.name,'wb') as f:
        for line in filename.chunks():
            f.write(line)
    return HttpResponse('上传成功.')

def img_1(request):
    '''
    图片预览1
    :param request:
    :return:
    '''
    if request.method=='GET':
        return render(request,'img_1.html')

def img_2(request):
    '''
    图片预览2
    :param request:
    :return:
    '''
    if request.method=="GET":
        return render(request,'img_2.html')

def img_3(request):
    '''
    图片预览3
    :param request:
    :return:
    '''
    if request.method=='GET':
        return render(request,'img_3.html')

def img_ajax(request):
    '''
    图片的预览ajax处理
    :param request:
    :return:
    '''
    if request.method=='POST':
        # ret={'status':True,'error':None,'data':None}
        # try:
        #     img_upload=request.FILES.get('img_upload')
        #     file_name=str(uuid.uuid4())+"."+img_upload.name.rsplit('.',maxsplit=1)[1]
        #     file_path='/static/'+'img/'+file_name
        #     with open(file_path,'wb') as f:
        #         for line in img_upload.chunks():
        #             f.write(line)
        #     ret['data']=file_path
        #     print( ret['data'])
        # except Exception as e:
        #     ret['status']=False
        #     ret['error']=e
        # #return JsonResponse(ret)
        # return HttpResponse(json.dumps(file_path))
        img_upload = request.FILES.get('img_upload')
        file_name = str(uuid.uuid4()) + "." + img_upload.name.rsplit('.', maxsplit=1)[1]
        img_file_path = os.path.join('static', 'img', file_name)
        with open(img_file_path, 'wb') as f:
            for line in img_upload.chunks():
                f.write(line)

        return HttpResponse(img_file_path)

def img_4(request):
    '''
    图片预览4
    :param request:
    :return:
    '''
    if request.method=='GET':
        return render(request,'img_4.html')
    if request.method=='POST':
        USER_LIST=[]
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        avatar = request.POST.get('avatar')
        print(avatar)
        USER_LIST.append(
            {
                'user': user,
                'pwd': pwd,
                'avatar': avatar
            }
        )
        request.session['user_list']=USER_LIST
        return redirect('/index/')
def img_iframe(request):
    '''
    图片预览iframe的处理方式
    :param request:
    :return:
    '''
    ret={'status':True,'data':None,'error':None}
    try:
        avatar=request.FILES.get('avatar')
        img_name=str(uuid.uuid4())+'.'+avatar.name.rsplit('.',maxsplit=1)[1]
        img_path=os.path.join('static','img',img_name)
        with open(img_path,'wb') as f:
            for line in avatar.chunks():
                f.write(line)

        ret['data']=img_path
    except Exception as e:
        ret['status']=False
        ret['error']='上传失败'
    return  HttpResponse(json.dumps(ret))

def index(request):
    return HttpResponse('ok')