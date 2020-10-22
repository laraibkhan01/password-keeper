# I created this file - Laraib

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html');

# def about(request):
#     return HttpResponse("about Laraib");

# def home(request):
#     return HttpResponse(''' <h1> Home Page </h1>
#     <a href = "http://127.0.0.1:8000/index" > click here to go index </a> <br>
#     ''')
def signin(request):
    return HttpResponse("New User")

def analyze(request):
    djtext = request.GET.get('text','default')
    newuser_bool = request.GET.get('new_user','not')
    if(newuser_bool == 'new_user'):
        return HttpResponse('''<a href = "http://127.0.0.1:8000/signin"> </a>''')
    removepunc = request.GET.get('removepunc','off')
    punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    if removepunc == 'on':
        for char in djtext:
            if(char not in punc):
                analyzed += char
        analyzed_text = djtext
        params = {'purpose' : djtext , 'analyzed_text' : analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")



    # return HttpResponse('''
    # <h1> Remove Punctuations </h1>
    # <a href = "http://127.0.0.1:8000/" > click here to go home </a> <br> ''')