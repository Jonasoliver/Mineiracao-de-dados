# Exercicio 6 - Razao de Comprometimento (Divida / Renda) - Feature de Credito
# Disciplina: Mineracao de Dados - Unidade 10

import pandas as pd

def razao_comprometimento(divida: float, renda: float) -> float:
    if renda is None or renda <= 0:
        return float("inf")  # Renda zero/negativa ja sinaliza risco maximo
    return round(divida / renda, 4)

def faixa_risco(razao: float) -> str:
    if razao == float("inf"):
        return "Indefinido (renda zero)"
    if razao < 0.30:
        return "Baixo"
    if razao < 0.50:
        return "Moderado"
    if razao < 0.80:
        return "Alto"
    return "Critico"

if __name__ == "__main__":
    clientes = pd.DataFrame([
        {"id": 1, "divida": 1500, "renda": 5000},   # 30%
        {"id": 2, "divida": 4000, "renda": 5000},   # 80%
        {"id": 3, "divida": 800,  "renda": 5000},   # 16%
        {"id": 4, "divida": 1500, "renda": 2000},   # 75%
        {"id": 5, "divida": 1500, "renda": 0},      # indefinido
    ])
    clientes["razao_comp"] = clientes.apply(
        lambda r: razao_comprometimento(r["divida"], r["renda"]), axis=1
    )
    clientes["faixa_risco"] = clientes["razao_comp"].apply(faixa_risco)
    print(clientes.to_string(index=False))

    print("""
JUSTIFICATIVA:
A razao Divida/Renda e mais valiosa do que as variaveis isoladas porque
relativiza a divida ao poder de pagamento. Um cliente com R$ 4.000 de
divida pode ser saudavel se ganha R$ 50.000, mas critico se ganha R$ 5.000.
Modelos que recebem so divida ou so renda nao capturam essa interacao;
a razao consolida o sinal em uma unica feature mais informativa e
mais resistente a outliers absolutos.
""")
