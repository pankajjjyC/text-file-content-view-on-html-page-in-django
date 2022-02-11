from django.shortcuts import render
from django.http import HttpResponse

def readfiles(request):     
    f=open('textfiles/file1.txt','r')
    file_content=f.readlines()
    f.close()    
    context={'file_content':file_content}
    return render(request, 'index.html', context)

def readfiles_ar(request,no1,no2):     
    f=open('textfiles/file1.txt','r')
    file_content=f.readlines()
    f.close()  
    num1=int(no1)
    num2=int(no2)+1 
    context={'file_content':file_content[num1:num2]}
    return render(request, 'index.html', context)

def readfiles2(request):     
    f=open('textfiles/file2.txt','r')
    file_content=f.readlines()
    f.close()    
    context={'file_content':file_content}
    return render(request, 'index.html', context)

def readfiles2_ar(request,no1,no2):     
    f=open('textfiles/file2.txt','r')
    file_content=f.readlines()
    f.close()  
    num1=int(no1)
    num2=int(no2)+1 
    context={'file_content':file_content[num1:num2]}
    return render(request, 'index.html', context)

def readfiles3(request):     
    f=open('textfiles/file3.txt','r')
    file_content=f.readlines()
    f.close()    
    context={'file_content':file_content}
    return render(request, 'index.html', context)

def readfiles3_ar(request,no1,no2):     
    f=open('textfiles/file3.txt','r')
    file_content=f.readlines()
    f.close()  
    num1=int(no1)
    num2=int(no2)+1 
    context={'file_content':file_content[num1:num2]}
    return render(request, 'index.html', context)

def readfiles4(request):     
    f=open('textfiles/file4.txt','r')
    file_content=f.readlines()
    f.close()    
    context={'file_content':file_content}
    return render(request, 'index.html', context)

def readfiles4_ar(request,no1,no2):     
    f=open('textfiles/file4.txt','r')
    file_content=f.readlines()
    f.close()  
    num1=int(no1)
    num2=int(no2)+1 
    context={'file_content':file_content[num1:num2]}
    return render(request, 'index.html', context)


'''def readfiles(request):     
    f=open('textfiles/file1.txt','r')
    d=f.read()
    f.close()  
    print(d)  
    
    return render(request, 'index.html', {'dat':d})'''


