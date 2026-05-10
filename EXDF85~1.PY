# Exercicio 8 - Ranking Interno por volume de vendas
# Disciplina: Mineracao de Dados - Unidade 10

import pandas as pd

def gerar_ranking(df: pd.DataFrame, coluna_valor: str, grupo: str | None = None) -> pd.DataFrame:
    df = df.copy()
    if grupo:
        df["ranking_interno"] = df.groupby(grupo)[coluna_valor].rank(
            method="dense", ascending=False
        ).astype(int)
        df["percentil"] = df.groupby(grupo)[coluna_valor].rank(pct=True).round(3)
    else:
        df["ranking_interno"] = df[coluna_valor].rank(method="dense", ascending=False).astype(int)
        df["percentil"] = df[coluna_valor].rank(pct=True).round(3)
    return df.sort_values(["ranking_interno"]) if grupo is None else df.sort_values([grupo, "ranking_interno"])

if __name__ == "__main__":
    vendas = pd.DataFrame([
        {"produto": "A", "categoria": "Eletronicos", "vendas": 1200},
        {"produto": "B", "categoria": "Eletronicos", "vendas":  900},
        {"produto": "C", "categoria": "Eletronicos", "vendas": 1500},
        {"produto": "D", "categoria": "Vestuario",   "vendas":  450},
        {"produto": "E", "categoria": "Vestuario",   "vendas":  780},
        {"produto": "F", "categoria": "Vestuario",   "vendas":  300},
    ])
    print("Ranking GLOBAL:")
    print(gerar_ranking(vendas, "vendas").to_string(index=False))

    print("\nRanking POR CATEGORIA:")
    print(gerar_ranking(vendas, "vendas", grupo="categoria").to_string(index=False))
