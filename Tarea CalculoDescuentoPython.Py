def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento y el monto final a pagar.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (default es 10%).
    :return: Monto del descuento y monto final a pagar.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final

def main():
    # Primera llamada a la función
    monto1 = 250  # Monto total de la compra
    descuento1, monto_final1 = calcular_descuento(monto1)
    print(f"Compra de ${monto1:.2f}:")
    print(f"Descuento: ${descuento1:.2f}")
    print(f"Monto a pagar: ${monto_final1:.2f}\n")

    # Segunda llamada a la función con un porcentaje de descuento diferente
    monto2 = 400  # Monto total de la compra
    porcentaje_descuento2 = 15  # Porcentaje de descuento diferente
    descuento2, monto_final2 = calcular_descuento(monto2, porcentaje_descuento2)
    print(f"Compra de ${monto2:.2f} con descuento del {porcentaje_descuento2}%:")
    print(f"Descuento: ${descuento2:.2f}")
    print(f"Monto a pagar: ${monto_final2:.2f}")

if __name__ == "__main__":
    main()
python CalculoDescuentoPython.py
Compra de $250.00:
Descuento: $25.00
Monto a pagar: $225.00

Compra de $400.00 con descuento del 15%:
Descuento: $60.00
Monto a pagar: $340.00
git init
git remote add origin <URL_DE_TU_REPOSITORIO>
git add CalculoDescuentoPython.py
git commit -m "Añadir programa de cálculo de descuento"
git push origin main
