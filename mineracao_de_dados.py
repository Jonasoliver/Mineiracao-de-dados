"""
Dependências:
pip install pandas numpy scipy scikit-learn
"""

import numpy as np
import pandas as pd
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler


def exercicio_1():
    print("\n" + "=" * 60)
    print("EXERCÍCIO 1 - Z-Score em temperaturas")
    print("=" * 60)

    temp = [45.5, 46.0, 45.2, 45.8, 46.1, 98.0, 45.9, 45.3]
    z_temp = zscore(temp)

    print("Temperaturas:", temp)
    print("Z-Scores:", np.round(z_temp, 2))

    print("\nAnomalias (Z-Score > 2.5):")
    encontrou = False
    for valor, z in zip(temp, z_temp):
        if z > 2.5:
            print(f"Temperatura: {valor} | Z-Score: {z:.2f}")
            encontrou = True

    if not encontrou:
        print("Nenhuma anomalia encontrada.")


def exercicio_2():
    print("\n" + "=" * 60)
    print("EXERCÍCIO 2 - Z-Score em voltagem")
    print("=" * 60)

    voltagem = [3.3, 3.2, 3.3, 3.4, 3.3, 1.2, 3.2, 3.3]
    z_voltagem = zscore(voltagem)

    print("Voltagens:", voltagem)
    print("Z-Scores:", np.round(z_voltagem, 2))

    if any(z < -2.0 for z in z_voltagem):
        print("\nFalha de Energia!")
    else:
        print("\nNenhuma falha detectada.")



def exercicio_5():
    print("\n" + "=" * 60)
    print("EXERCÍCIO 5 - Isolation Forest em servidores")
    print("=" * 60)

    servidores = [[20, 30], [25, 35], [22, 32], [99, 95], [21, 31]]

    modelo = IsolationForest(random_state=42, contamination=0.2)
    modelo.fit(servidores)
    predicoes = modelo.predict(servidores)

    print("Servidores:", servidores)
    print("Predições:", predicoes)
    print("No Isolation Forest: 1 = normal | -1 = anomalia")



def exercicio_7():
    print("\n" + "=" * 60)
    print("EXERCÍCIO 7 - Análise multivariada de alunos")
    print("=" * 60)

    alunos = [[8, 2], [7, 4], [9, 1], [8, 3], [2, 25], [9, 25]]

    modelo = IsolationForest(contamination=0.34, random_state=42)
    predicoes = modelo.fit_predict(alunos)

    for aluno, pred in zip(alunos, predicoes):
        print(f"Aluno {aluno} -> {'Anomalia' if pred == -1 else 'Normal'}")


def exercicio_11():
    print("\n" + "=" * 60)
    print("EXERCÍCIO 11 - Normalização com valores negativos")
    print("=" * 60)

    temps = [[-20], [-10], [0], [20]]

    scaler = MinMaxScaler()
    temps_norm = scaler.fit_transform(temps)

    print("Temperaturas originais:")
    print(np.array(temps).flatten())

    print("\nTemperaturas normalizadas:")
    print(temps_norm.flatten())

    print("\nExplicação:")
    print("O valor 0°C original não permanece 0 após a normalização.")
    print("Na nova escala, 0.0 representa o menor valor do conjunto, que é -20°C.")


def exercicio_12():
    print("\n" + "=" * 60)
    print("EXERCÍCIO 12 - Remoção de outlier e normalização")
    print("=" * 60)

    producao = [100, 102, 98, 105, 500, 101]
    z_producao = zscore(producao)

    indice_outlier = np.argmax(np.abs(z_producao))
    valor_outlier = producao[indice_outlier]

    producao_limpa = [v for i, v in enumerate(producao) if i != indice_outlier]

    scaler = MinMaxScaler()
    producao_norm = scaler.fit_transform(np.array(producao_limpa).reshape(-1, 1))

    print("Produção original:", producao)
    print("Z-Scores:", np.round(z_producao, 2))
    print("Outlier removido:", valor_outlier)
    print("Produção limpa:", producao_limpa)
    print("Produção normalizada:", producao_norm.flatten().tolist())

    print("\nExplicação:")
    print("É melhor remover outliers antes de normalizar.")
    print("Se o valor 500 permanecesse, ele achataria os demais valores perto de 0 na escala.")


def main():
    # Tópico 1
    exercicio_1()
    exercicio_2()

    # Tópico 2
    exercicio_5()
    exercicio_7()

    # Tópico 3
    exercicio_9()
    exercicio_11()
    exercicio_12()


if __name__ == "__main__":
    main()
