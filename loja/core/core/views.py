from django.shortcuts import render, redirect


def login(request):
    return render(request, 'login.html')


def pagina_inexistente(request, exception):  # precisa ser exception
    return render(request, 'pagina-inexistente.html')
