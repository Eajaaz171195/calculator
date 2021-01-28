from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    context = { 'r_numb1': '0'
                ,'r_numb2': '0'
                }
    return render(request,'index.html', context)

def submitquery(request):
    number_1 = request.POST.get('numb1', False)
    number_2 = request.POST.get('numb2', False)
    if number_1 is not '' and number_2 is not '':
        n1 = int(number_1)
        n2 = int(number_2)
        if 'add_nums' in request.POST:
            result = n1+n2
        elif 'sub_nums' in request.POST:
            result = n1-n2
        elif 'mul_nums' in request.POST:
            result = n1*n2
        elif 'div_nums' in request.POST:
            if n2 == 0:
                result = 'Bad Request'
            else:
                result = n1/n2
    else:
        result = 'Inputs cannot be Empty'
        n1 = '0' if number_1 == '' else number_1
        n2 = '0' if number_2 == '' else number_2
    context = { 'r_result': str(result)
                   ,'r_numb1': str(n1)
                   ,'r_numb2': str(n2)
                            }
    return render(request,'index.html', context)        
