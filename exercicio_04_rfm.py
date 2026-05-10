# Exercicio 4 - Resumo de perfil RFM (Recencia, Frequencia, Monetario)
# Disciplina: Mineracao de Dados - Unidade 10
#
# Transforma um log transacional (id_cliente, data, valor) num resumo
# de UM registro por cliente contendo as 3 dimensoes do modelo RFM.

import pandas as pd
from datetime import datetime

def calcular_rfm(transacoes: pd.DataFrame, data_referencia=None) -> pd.DataFrame:
    df = transacoes.copy()
    df["data"] = pd.to_datetime(df["data"])
    if data_referencia is None:
        data_referencia = df["data"].max()
    else:
        data_referencia = pd.to_datetime(data_referencia)

    rfm = df.groupby("id_cliente").agg(
        recencia=("data", lambda x: (data_referencia - x.max()).days),
        frequencia=("data", "count"),
        monetario=("valor", "sum"),
    ).reset_index()
    return rfm

if __name__ == "__main__":
    log = pd.DataFrame([
        {"id_cliente": 1, "data": "2026-04-10", "valor": 150.00},
        {"id_cliente": 1, "data": "2026-04-25", "valor": 230.50},
        {"id_cliente": 1, "data": "2026-05-05", "valor":  90.00},
        {"id_cliente": 2, "data": "2026-01-20", "valor": 420.00},
        {"id_cliente": 2, "data": "2026-02-15", "valor": 310.00},
        {"id_cliente": 3, "data": "2026-05-08", "valor":  55.00},
        {"id_cliente": 3, "data": "2026-05-09", "valor":  60.00},
        {"id_cliente": 3, "data": "2026-05-10", "valor":  75.00},
    ])
    rfm = calcular_rfm(log, data_referencia="2026-05-10")
    print(rfm.to_string(index=False))
