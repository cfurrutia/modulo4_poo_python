from medicamento import Medicamento

paracetamol = Medicamento()
aspirina = Medicamento()

print(paracetamol.descuento)
print(aspirina.descuento)

paracetamol.descuento = 0.06

print(paracetamol.descuento)
print(aspirina.descuento)