# from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def index(request: HttpRequest):
    user_agent = request.META["HTTP_USER_AGENT"]

    responce = HttpResponse()
    responce.write(f"<h1> Эта страница исходная</h1>"
                        f"<a href={"hello"}> перейти на страницу Hello</a>"
                        f"</br>"
                        f"User_agent:{user_agent}"
                        f"</br>"
                        f"<a href = {"about"}>Перейти на About</a>")
    # responce.status_code = 200
    responce.headers["content-type"] = "text/html; charset=utf-8"
    return responce


def hello_world(request):
    return HttpResponse(f"<h1>Hello World</h1>"
                        f"<a href = {"../"}>Назад</a>")

def about_us(request):
    return HttpResponse(f"<h1 style = 'color: blue;"
                        f" text-shadow: 7px 4px 3px rgba(0, 0, 0, 0.105);'>Hello On Our Site!</h1>"
                        f"<a href = {'../'}>Назад</a>")