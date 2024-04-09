from medicamento import Medicamento

paracetamol = Medicamento()
aspirina = Medicamento()

print(paracetamol.descuento)
print(aspirina.descuento)

paracetamol.descuento = 0.06

print(paracetamol.descuento)
print(aspirina.descuento)

Medicamento.descuento = 0.04
ibuprofeno = Medicamento()
print(ibuprofeno.descuento)

precio = int(input("Ingrese un precio a validar:\n"))
es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido:
    print("El precio ingresado es válido")
else:
    print("El precio ingresado no es válido")

if paracetamol.IVA == aspirina.IVA and paracetamol.descuento == aspirina.descuento:
    print("todas las instancias, tienen los mismos valores de IVA y descuento")
    print("El valor del IVA es", Medicamento.IVA)
    print("El valor de descuento es", Medicamento.descuento)
    
ibuprofeno.modificar_atributo()
print(ibuprofeno.IVA)   # no cambia

