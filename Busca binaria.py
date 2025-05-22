import pandas as pd
import time
import psutil
import os

def busca_binaria(df, Genero):  # Busca binária na coluna 'Genero'
    inicio, fim = 0, len(df) - 1
    encontrados = []

    while inicio <= fim:
        meio = (inicio + fim) // 2
        genero = df.iloc[meio][Genero]

        if genero.lower() == 'm':
            encontrados.append(df.iloc[meio])
            i = meio - 1
            while i >= 0 and df.iloc[i][Genero].lower() == 'm':
                encontrados.append(df.iloc[i])
                i -= 1

            i = meio + 1
            while i < len(df) and df.iloc[i][Genero].lower() == 'm':
                encontrados.append(df.iloc[i])
                i += 1
            break
        elif genero.lower() < 'm':
            inicio = meio + 1
        else:
            fim = meio - 1

    return pd.DataFrame(encontrados)

# Iniciar o monitoramento de tempo e memória
start_time = time.time()

# Iniciar o monitoramento de memória
process = psutil.Process(os.getpid())
mem_inicial = process.memory_info().rss / 1024 ** 2  # Em MB

# Lê os dados do arquivo e ordena
df = pd.read_excel('Cadastro Clientes.xlsx')
df_ordenado = df.sort_values(by='Genero').reset_index(drop=True)

# Executa a busca binária
resultado = busca_binaria(df_ordenado, 'Genero')

# Finaliza o monitoramento de memória
mem_final = process.memory_info().rss / 1024 ** 2  # Em MB

# Calcula o tempo de execução
end_time = time.time()

# Agora, exibe as informações sobre o tempo de execução e uso de memória
print(f"\nTempo de execução: {end_time - start_time:.4f} segundos")
print(f"Memória inicial: {mem_inicial:.2f} MB")
print(f"Memória final: {mem_final:.2f} MB")

# Exibe o resultado da busca binária
print("\nResultado da busca binária:")
print(resultado)
