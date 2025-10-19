#!/usr/bin/env python3

def classificar_imc(peso: float, altura: float) -> str:
    imc = peso / (altura ** 2)
    if imc < 17:
        categoria = "Está MUITO ABAIXO DO PESO IDEAL!"
    elif 17 <= imc < 18.5:
        categoria = "Está ABAIXO DO PESO IDEAL!"
    elif 18.5 <= imc < 25:
        categoria = "Está no PESO IDEAL!"
    elif 25 <= imc < 30:
        categoria = "Está com SOBREPESO!"
    elif 30 <= imc < 35:
        categoria = "Está com OBESIDADE!"
    elif 35 <= imc < 40:
        categoria = "Está com OBESIDADE SEVERA!"
    else:
        categoria = "Está com OBESIDADE MORBIDA!"
    return f"Seu IMC é {imc:.2f}. {categoria}"

def main():
    try:
        p = float(input("Digite seu peso: "))
        a = float(input("Digite sua altura: "))
        if a <= 0:
            print("Altura inválida. Deve ser um número maior que zero.")
            return
        print(classificar_imc(p, a))
    except ValueError:
        print("Entrada inválida. Digite números válidos para peso e altura.")

if __name__ == "__main__":
    main()