from django.shortcuts import render

# Create your views here.
# 添加index 函数，返回index.html 页面
def index(request):
	return render(request,'index.html')

def hello(request):
	context={}
	context['hello']='hello world'
	return render(request,'hello.html',context)