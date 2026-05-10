# Exercicio 2 - Decomposicao de timestamps e flag de fim de semana
# Disciplina: Mineracao de Dados - Unidade 10

import pandas as pd

DIAS_SEMANA_PT = {
    0: "Segunda", 1: "Terca", 2: "Quarta", 3: "Quinta",
    4: "Sexta", 5: "Sabado", 6: "Domingo",
}

def decompor_timestamps(timestamps: list[str]) -> pd.DataFrame:
    df = pd.DataFrame({"timestamp": pd.to_datetime(timestamps)})
    df["mes"] = df["timestamp"].dt.month
    df["dia_semana_num"] = df["timestamp"].dt.dayofweek  # 0=segunda
    df["dia_semana"] = df["dia_semana_num"].map(DIAS_SEMANA_PT)
    # Flag = 1 se sabado (5) ou domingo (6)
    df["flag_fim_de_semana"] = df["dia_semana_num"].isin([5, 6]).astype(int)
    return df

if __name__ == "__main__":
    acessos = [
        "2026-05-04 09:15:00",  # Segunda
        "2026-05-09 22:30:00",  # Sabado
        "2026-05-10 11:00:00",  # Domingo
        "2026-12-25 08:00:00",  # Sexta (Natal)
        "2026-07-15 14:20:00",  # Quarta
    ]
    df = decompor_timestamps(acessos)
    print(df.to_string(index=False))
