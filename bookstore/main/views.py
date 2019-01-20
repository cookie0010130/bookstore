from django.shortcuts import render



def main(request):
    '''
    Render the main page
    '''
    return render(request, 'main/main.html')

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')

def login(request):
    '''
    Render the about page
    '''
    return render(request, 'main/login.html')

def aboutbookstore(request):
    '''
    Render the about page
    '''
    return render(request, 'main/aboutbookstore.html')

def personal(requset):
    return render(requset,'main/personal.html')

def new(requset):
    return render(requset,'main/new.html')

def hot(requset):
    return render(requset,'main/hot.html')

def saleoff(requset):
    return render(requset,'main/34off.html')

def title1(requset):
    return render(requset,'main/title1.html')

def title2(requset):
    return render(requset,'main/title2.html')

def title3(requset):
    return render(requset,'main/title3.html')

def title4(requset):
    return render(requset,'main/title4.html')

def book1(requset):
    return render(requset,'main/book1.html')

def book2(requset):
    return render(requset,'main/book2.html')

def book3(requset):
    return render(requset,'main/book3.html')

def book4(requset):
    return render(requset,'main/book4.html')


