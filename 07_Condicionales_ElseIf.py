Ingreso_Empresa1 = 50000
Gasto_Empresa1 = 3500

Ingreso_Empresa2 = 30000
Gasto_Empresa2 = 45000

#En python el else if se escribe como "elif"

if Gasto_Empresa1 == Ingreso_Empresa1:
    print("Estas en Status Quo en cuanto a ganancias y gastos")
elif Gasto_Empresa1 > Ingreso_Empresa1:
    print("Estas en deficit")
elif Ingreso_Empresa1-Gasto_Empresa1 < 5000:
    print("Estas ganando poco")
elif Ingreso_Empresa1-Gasto_Empresa1 < 15000:
    print("Estas ganando lo Justo para mantener la empresa")
elif Ingreso_Empresa1-Gasto_Empresa1 < 25000:
    print("Tu empresa es estable economicamente hablando")
else:
    print("Estas ganando lo suficiente como para expandir tu empresa")
    




