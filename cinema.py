import os

# Programa simples de reserva de cadeiras (em português)


NUM_CADEIRAS = 10
cadeiras = [""] * NUM_CADEIRAS  # "" = livre, "X" = ocupada

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def mostra_fileira():
    for i in range(NUM_CADEIRAS):
        if cadeiras[i] == "":
            print(f"[ B{i+1:2} ]", end=" ")
        else:
            print("[ --- ]", end=" ")
    print()
    print("-" * 72)

def main():
    resposta = "S"
    while resposta.upper() != "N":
        limpar_tela()
        mostra_fileira()
        entrada = input("Reservar a cadeira: B").strip()
        try:
            cad = int(entrada)
            if 1 <= cad <= NUM_CADEIRAS:
                if cadeiras[cad - 1] == "":
                    cadeiras[cad - 1] = "X"
                    print(f"Cadeira B{cad} RESERVADA!")
                else:
                    print("ERRO: Lugar ocupado!")
            else:
                print(f"ERRO: Informe um número entre 1 e {NUM_CADEIRAS}.")
        except ValueError:
            print("ERRO: Entrada inválida. Digite o número da cadeira (ex: 3).")
        resposta = input("Quer reservar outro? [S/N] ").strip().upper()
    print("\nSituação final:")
    mostra_fileira()

if __name__ == "__main__":
    main()