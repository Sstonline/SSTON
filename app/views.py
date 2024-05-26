from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, "base.html")
def home(request):
    return render(request, "home/home.html")
def relato(request):
    return render(request, "relatos/relato.html")
def dash(request):
    return render(request, "dashboard/dash.html")
def gestao(request):
    return render(request, "gestao/gestao.html")
def config(request):
    return render(request, "config/config.html")

def n_relato(request):
    return render(request, "relatos/n_relato.html")
def estra(request):
    return render(request, "relatos/estra.html")
def l_relatos(request):
    return render(request, "relatos/l_relato.html")
def l_estra(request):
    return render(request, "relatos/l_estra.html")

def user(request):
    return render(request, "gestao/user.html")
def unidade(request):
    return render(request, "gestao/unidade.html")
def turno(request):
    return render(request, "gestao/turno.html")
def setor(request):
    return render(request, "gestao/setor.html")
def cargo(request):
    return render(request, "gestao/cargo.html")

def d_rel(request):
    return render(request, "dashboard/d_rel.html")
def d_estra(request):
    return render(request, "dashboard/d_rel.html")