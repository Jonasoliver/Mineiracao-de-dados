# Exercicio 1 - Extracao de dominio de e-mail e flag de provedor comum/empresarial
# Disciplina: Mineracao de Dados - Unidade 10

import pandas as pd

# Lista de provedores considerados "comuns" (pessoais)
PROVEDORES_COMUNS = {
    "gmail.com", "hotmail.com", "outlook.com", "yahoo.com",
    "yahoo.com.br", "live.com", "icloud.com", "bol.com.br",
    "uol.com.br", "terra.com.br"
}

def extrair_dominio(email: str) -> str:
    """Retorna o dominio (parte apos o @) em caixa baixa."""
    if not isinstance(email, str) or "@" not in email:
        return ""
    return email.strip().lower().split("@")[-1]

def classificar_email(email: str) -> dict:
    dominio = extrair_dominio(email)
    # Flag = 1 se for provedor comum, 0 se parecer infraestrutura empresarial
    flag_comum = 1 if dominio in PROVEDORES_COMUNS else 0
    # Flag empresarial: dominios que terminam em .com.br ou nao sao provedores comuns
    flag_empresarial = 0 if flag_comum else 1
    return {
        "email": email,
        "dominio": dominio,
        "flag_provedor_comum": flag_comum,
        "flag_empresarial": flag_empresarial,
    }

if __name__ == "__main__":
    emails = [
        "joao.silva@gmail.com",
        "maria@empresa.com.br",
        "contato@startup.io",
        "user@hotmail.com",
        "rh@bancodobrasil.com.br",
        "vendas@yahoo.com",
    ]
    df = pd.DataFrame([classificar_email(e) for e in emails])
    print(df.to_string(index=False))
