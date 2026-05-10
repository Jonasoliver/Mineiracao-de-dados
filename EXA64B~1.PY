# Exercicio 7 - Indicador de Omissao antes do preenchimento de NaN
# Disciplina: Mineracao de Dados - Unidade 10
#
# Cria uma flag *_foi_omisso para preservar a informacao de que o campo
# estava vazio antes de aplicar a imputacao (mediana, media, etc.).

import pandas as pd
import numpy as np

def tratar_nulos_com_flag(df: pd.DataFrame, colunas: list[str], estrategia: str = "mediana") -> pd.DataFrame:
    df = df.copy()
    for col in colunas:
        flag = f"{col}_foi_omisso"
        df[flag] = df[col].isna().astype(int)

        if estrategia == "mediana":
            valor = df[col].median()
        elif estrategia == "media":
            valor = df[col].mean()
        elif estrategia == "zero":
            valor = 0
        else:
            raise ValueError("Estrategia desconhecida")

        df[col] = df[col].fillna(valor)
    return df

if __name__ == "__main__":
    dados = pd.DataFrame({
        "id":      [1, 2, 3, 4, 5],
        "renda":   [3500, np.nan, 8000, 5200, np.nan],
        "idade":   [25, 32, np.nan, 41, 29],
    })
    print("ANTES:")
    print(dados.to_string(index=False))

    tratado = tratar_nulos_com_flag(dados, ["renda", "idade"], estrategia="mediana")
    print("\nDEPOIS (com flag de omissao):")
    print(tratado.to_string(index=False))
