from django.shortcuts import render,redirect,reverse,HttpResponse
from publisher_list import models
from django.views import View

##展示出版社
def publisher_list(request):
    #查询所有出版社对象
    all_publisher = models.Publisher.objects.all()
    return render(request,'all_publisher.html',{'all_publisher':all_publisher})


def publisher_add(request):
    if request.method == 'POST':
        ##获取提交数据
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request,'publisher_add.html',{'error':'名称不能为空'})
        #插入数据库
        models.Publisher.objects.create(name=pub_name)

        return redirect(reverse('all_pub'))

    return render(request,'publisher_add.html')


def publisher_delete(request):
    #获取提交的数据
    pk = request.GET.get('pk')
    #删除对应的数据
    models.Publisher.objects.filter(pk=pk).delete()  ##删除符合条件的多个条目也可以用get

    return redirect(reverse('all_pub'))

def publisher_edit(request):
    # 获取提交的数据
    pk = request.GET.get('pk')
    # 查找需要编辑的对象
    obj = models.Publisher.objects.get(pk=pk)

    if request.method == 'POST':
        ##获取新提交的数据
        pub_name = request.POST.get('pub_name')
        obj.name = pub_name
        obj.save()

        return redirect(reverse('all_pub'))

    return render(request, 'publisher_edit.html', {'obj': obj})

def book(request):
    all_book = models.Book.objects.all()

    return render(request,'book.html',{'all_book':all_book})

class book_add(View):

    def get(self,request):

        all_pub = models.Publisher.objects.all()
        return render(request,'book_add.html',{'all_pub': all_pub})

    def post(self,request):

        #获取参数
        title = request.POST.get('title')
        pub_id = request.POST.get('pub_id')
        #插入数据到数据库
        models.Book.objects.create(title=title,pub_id=pub_id)

        return redirect(reverse('book'))

class book_edit(View):

    def get(self,request,pk):

        book_obj = models.Book.objects.get(pk=pk)
        all_pub = models.Publisher.objects.all()
        return render(request,'book_edit.html',{'book_obj':book_obj, 'all_pub':all_pub})

    def post(self,request,pk):
        book_obj = models.Book.objects.get(pk=pk)
        #获取参数
        title = request.POST.get('title')
        pub_id = request.POST.get('pub_id')
        #插入数据到数据库
        # book_obj.title = title
        # book_obj.pub_id = pub_id
        # book_obj.save()
        models.Book.objects.filter(pk=pk).update(title=title,pub_id=pub_id)
        return redirect(reverse('book'))

def book_del(request,pk):
    book_obj = models.Book.objects.get(pk=pk)
    book_obj.delete()
    return redirect(reverse('book'))