"Calcula el Índice de Masa Corporal (IMC)."

def main():
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))

    imc = peso / (altura * altura)

    print(f"Tu IMC es: {imc:.2f}")


if __name__ == "__main__":
    main()
