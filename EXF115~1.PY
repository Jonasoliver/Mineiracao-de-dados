# Exercicio 10 - Delta do Delta (aceleracao) e alerta de tendencia exponencial
# Disciplina: Mineracao de Dados - Unidade 10

def analisar_aceleracao(leituras: list[float]) -> dict:
    if len(leituras) < 3:
        raise ValueError("Sao necessarias pelo menos 3 leituras.")
    l1, l2, l3 = leituras[-3], leituras[-2], leituras[-1]
    delta_1 = l2 - l1   # variacao da 1a para a 2a
    delta_2 = l3 - l2   # variacao da 2a para a 3a
    aceleracao = delta_2 - delta_1   # delta do delta

    # Alerta = 1 se ambos os deltas forem positivos E a aceleracao tambem
    # (ritmo crescente acelerando = padrao exponencial)
    alerta = int(delta_1 > 0 and delta_2 > 0 and aceleracao > 0)

    return {
        "leituras": leituras[-3:],
        "delta_1": round(delta_1, 4),
        "delta_2": round(delta_2, 4),
        "aceleracao": round(aceleracao, 4),
        "alerta_exponencial": alerta,
    }

if __name__ == "__main__":
    cenarios = {
        "Crescimento exponencial":   [10, 12, 16],   # 2, 4 -> acelerando
        "Crescimento linear":        [10, 15, 20],   # 5, 5 -> sem aceleracao
        "Crescimento desacelerando": [10, 18, 22],   # 8, 4 -> freando
        "Queda":                      [50, 40, 30],  # -10, -10
        "Estavel":                    [10, 10, 10],
    }
    for nome, leituras in cenarios.items():
        r = analisar_aceleracao(leituras)
        print(f"{nome:30s} -> {r}")
