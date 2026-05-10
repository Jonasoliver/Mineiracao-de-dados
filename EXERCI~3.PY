# Exercicio 3 - Flag de feriado / evento comercial
# Disciplina: Mineracao de Dados - Unidade 10
#
# Marca uma data de transacao com 1 quando coincide com feriado ou evento
# comercial conhecido. Isso evita que o pico de vendas seja interpretado
# como anomalia pelo modelo.

import pandas as pd
from datetime import date

# Feriados fixos (mes, dia) - validos para qualquer ano
FERIADOS_FIXOS = {
    (1, 1):  "Confraternizacao Universal",
    (4, 21): "Tiradentes",
    (5, 1):  "Dia do Trabalho",
    (9, 7):  "Independencia",
    (10, 12):"Nossa Senhora Aparecida",
    (11, 2): "Finados",
    (11, 15):"Proclamacao da Republica",
    (12, 25):"Natal",
    # Eventos comerciais
    (2, 14): "Dia dos Namorados (intl.)",
    (5, 12): "Dias das Maes (referencia 2o domingo de maio)",
    (6, 12): "Dia dos Namorados (BR)",
    (8, 11): "Dia dos Pais (referencia 2o domingo de agosto)",
    (10, 12):"Dia das Criancas",
}

# Datas variaveis - calculadas (Black Friday = ultima sexta de novembro)
def black_friday(ano: int) -> date:
    # Pega o ultimo dia de novembro e volta ate sexta-feira (4)
    d = date(ano, 11, 30)
    while d.weekday() != 4:
        d = d.replace(day=d.day - 1)
    return d

def cyber_monday(ano: int) -> date:
    bf = black_friday(ano)
    return date(ano, 12, 3) if bf.day >= 28 else date(ano, bf.month, bf.day + 3)

def verificar_evento(data_transacao) -> dict:
    d = pd.to_datetime(data_transacao).date()
    nome_evento = FERIADOS_FIXOS.get((d.month, d.day))
    if d == black_friday(d.year):
        nome_evento = "Black Friday"
    elif d == cyber_monday(d.year):
        nome_evento = "Cyber Monday"
    return {
        "data": d.isoformat(),
        "evento": nome_evento or "",
        "flag_evento": 1 if nome_evento else 0,
    }

if __name__ == "__main__":
    datas = [
        "2026-12-25",  # Natal
        "2026-11-27",  # Black Friday 2026
        "2026-07-04",  # Dia comum
        "2026-05-10",  # Domingo comum
        "2026-09-07",  # Independencia
    ]
    df = pd.DataFrame([verificar_evento(d) for d in datas])
    print(df.to_string(index=False))
