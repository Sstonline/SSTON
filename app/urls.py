from django.urls import path
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("home", views.home, name="home"),
    path("relato", views.relato, name="relato"),
    path("dash", views.dash, name="dash"),
    path("gestao", views.gestao, name="gestao"),
    path("config", views.config, name="config"),

    path("n_relato", views.n_relato, name="n_relato"),
    path("estra", views.estra, name="estra"),
    path("l_relatos", views.l_relatos, name="l_relatos"),
    path("l_estra", views.l_estra, name="l_estra"),

    path("user", views.user, name="user"),
    path("unidade", views.unidade, name="unidade"),
    path("turno", views.turno, name="turno"),
    path("setor", views.setor, name="setor"),
    path("cargo", views.cargo, name="cargo"),

    path("d_rel", views.d_rel, name="d_rel"),
    path("d_estra", views.d_estra, name="d_estra"),
]