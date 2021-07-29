from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict ={'text':'hello_world','number':100}
    return render(request,'reletive_urls/index.html',context=context_dict)
def other(request):
    return render(request,'reletive_urls/other.html')
def reletive(request):
    return render(request,'reletive_urls/reletive_url_template.html')