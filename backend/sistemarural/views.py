# sistemarural/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.db.models import Sum

from apps.alimentacao.models import Alimentacao
from apps.ordenha.models import Ordenha
from apps.reproducao.models import Reproducao
from apps.saude.models import Saude

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    usuario = request.user

    # Filtro de datas
    data_inicio = request.GET.get("inicio")
    data_fim = request.GET.get("fim")
    hoje = datetime.today().date()

    data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date() if data_inicio else hoje.replace(day=1)
    data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date() if data_fim else hoje
    dias = max((data_fim - data_inicio).days + 1, 1)

    # Dados por usuário
    alimentacao = Alimentacao.objects.filter(usuario=usuario, data__range=(data_inicio, data_fim))
    ordenha = Ordenha.objects.filter(usuario=usuario, data__range=(data_inicio, data_fim))
    reproducao = Reproducao.objects.filter(usuario=usuario, data__range=(data_inicio, data_fim))
    saude = Saude.objects.filter(usuario=usuario, data__range=(data_inicio, data_fim))

    # Cálculos ordenha
    total_leite = sum(o.quantidade_leite or 0 for o in ordenha)
    media_diaria = total_leite / dias

    grafico_data = []
    grafico_valores = []
    for i in range(dias):
        dia = data_inicio + timedelta(days=i)
        qtd = ordenha.filter(data=dia).aggregate(total_dia=Sum("quantidade_leite"))["total_dia"] or 0
        grafico_data.append(dia.strftime("%d/%m"))
        grafico_valores.append(float(qtd))

    # Reprodução e gestação
    ultima_reproducao = Reproducao.objects.filter(usuario=usuario).order_by('-data').first()
    progresso_gestacao = None
    if ultima_reproducao:
        dias_gestacao = (hoje - ultima_reproducao.data).days
        progresso_gestacao = min(round((dias_gestacao / 285) * 100), 100)

    # Vacinas (tipo='vacina' obrigatório)
    vacinas_atrasadas = Saude.objects.filter(usuario=usuario, tipo="vacina", proxima_dose__lt=hoje).count()
    vacinas_proximas = Saude.objects.filter(usuario=usuario, tipo="vacina", proxima_dose__gte=hoje).count()

    context = {
        # Cards
        "media": round(media_diaria, 2),
        "total_ordenha": ordenha.count(),
        "total_alimentacao": alimentacao.count(),
        "total_reproducao": reproducao.count(),
        "total_saude": saude.count(),

        # Gráfico
        "grafico_data": grafico_data,
        "grafico_valores": grafico_valores,

        # Filtros
        "inicio": data_inicio.strftime("%Y-%m-%d"),
        "fim": data_fim.strftime("%Y-%m-%d"),

        # Extras
        "ultima_reproducao": ultima_reproducao,
        "progresso_gestacao": progresso_gestacao,
        "vacinas_atrasadas": vacinas_atrasadas,
        "vacinas_proximas": vacinas_proximas,
    }

    return render(request, "dashboard.html", context)