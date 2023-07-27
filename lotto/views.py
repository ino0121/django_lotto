from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})

def post(request):
    if request.method == "POST":
        # print(request.POST)
        # print(request.method)
        # 사용자로부터 입력받은 POST 요청 데이터를 담아 PostForm 객체 생성
        form = PostForm(request.POST)
        # print(type(form))
        # print(form)
        if form.is_valid():
            # 사용자로부터 입력받은 form 데이터에서 추가로 수정해주려는 사항이 있을 경우 save를 보류
            lotto = form.save(commit=False)  # 최종 DB 저장은 아래 generate 함수 내부의 .save()로 처리
            print(type(lotto))  # <class 'lotto.models.GuesNumbers'>
            print(lotto)
            lotto.generate()
            return redirect('index')  # urls.py의 name='index'에 해당 -> 상단 from django.sortcuts import render, redirect 수정
    else:
        form = PostForm()  # empty form
        return render(request, 'lotto/form.html', {"form":form})


def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, "lotto/detail.html", {"lotto":lotto})


