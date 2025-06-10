import random

def rolar_dado(comando):
    try:
        # Separar a parte do modificador
        if '+' in comando:
            dado_part, sepSoma = comando.split('+')
            sepSoma = int(sepSoma)
        else:
            dado_part = comando
            sepSoma = 0

        # Separar quantidade e tipo de dado
        qtd_dados, tipo_dado = dado_part.split('d')
        qtd_dados = int(qtd_dados) if qtd_dados else 1  # Se não houver número antes do d, assume 1
        tipo_dado = int(tipo_dado)

        # Rolar os dados
        valor = [random.randint(1, tipo_dado) for _ in range(qtd_dados)]
        total = sum(valor) + sepSoma

        print(f"Resultados individuais: {valor}")
        print(f"Total com modificador: {total}")

    except (ValueError, AttributeError):
        print("Formato inválido. Use algo como '2d6+1' ou 'd20'.")

dado = input("Digite o dado para rolar (ex: 2d6+1): ")
rolar_dado(dado)