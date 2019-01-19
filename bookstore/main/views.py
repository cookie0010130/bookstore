from django.shortcuts import render



def main(request):
    '''
    Render the main page
    '''
    return render(request, 'main/main.html')

def login(request):
    '''
    Render the about page
    '''
    return render(request, 'main/login.html')

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')

def 登入(request):
    '''
    Render the about page
    '''
    return render(request, 'main/登入.html')

def 關於bookstore(request):
    '''
    Render the about page
    '''
    return render(request, 'main/關於bookstore.html')

def 隱私政策(requset):
    return render(requset,'main/隱私政策.html')

def 新品推薦(requset):
    return render(requset,'main/新品推薦.html')

def 暢銷書榜(requset):
    return render(requset,'main/暢銷書榜.html')

def 今日66折(requset):
    return render(requset,'main/今日66折.html')

def 經典文學(requset):
    return render(requset,'main/經典文學.html')

def 心理勵志(requset):
    return render(requset,'main/心理勵志.html')

def 推理文學(requset):
    return render(requset,'main/推理文學.html')

def 科幻小說(requset):
    return render(requset,'main/科幻小說.html')

def 傲慢與偏見(requset):
    return render(requset,'main/傲慢與偏見.html')

def 被討厭的勇氣(requset):
    return render(requset,'main/被討厭的勇氣.html')

def 福爾摩斯(requset):
    return render(requset,'main/福爾摩斯全集.html')

def harrypotter(requset):
    return render(requset,'main/harrypotter.html')


