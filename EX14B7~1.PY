# Exercicio 5 - Monitor de variacao de sensor (Delta + Evolucao Percentual)
# Disciplina: Mineracao de Dados - Unidade 10

def monitorar_sensor(leitura_t1: float, leitura_t2: float) -> dict:
    delta = leitura_t2 - leitura_t1
    if leitura_t1 == 0:
        evolucao_pct = float("inf") if delta != 0 else 0.0
    else:
        evolucao_pct = (delta / leitura_t1) * 100

    if delta > 0:
        tendencia = "Crescimento"
    elif delta < 0:
        tendencia = "Queda"
    else:
        tendencia = "Estavel"

    return {
        "leitura_t1": leitura_t1,
        "leitura_t2": leitura_t2,
        "delta": round(delta, 4),
        "evolucao_pct": round(evolucao_pct, 2),
        "tendencia": tendencia,
    }

if __name__ == "__main__":
    pares = [
        (100.0, 115.0),  # crescimento de 15%
        (80.5, 80.5),    # estavel
        (200.0, 150.0),  # queda
        (50.0, 75.0),    # crescimento de 50%
    ]
    print(f"{'t1':>8} {'t2':>8} {'delta':>10} {'evolucao_%':>12} {'tendencia':>14}")
    for t1, t2 in pares:
        r = monitorar_sensor(t1, t2)
        print(f"{r['leitura_t1']:>8} {r['leitura_t2']:>8} {r['delta']:>10} "
              f"{r['evolucao_pct']:>12} {r['tendencia']:>14}")
