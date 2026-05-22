# Problema 2 - Menú de restaurante con promoción

menu = [
    ["Hamburguesa", "Comida rápida", 18000],
    ["Pizza personal", "Comida rápida", 22000],
    ["Ensalada César", "Saludable", 16000],
    ["Jugo natural", "Bebidas", 8000],
    ["Limonada", "Bebidas", 7000],
    ["Salmón", "Plato fuerte", 35000]
]

CATEGORIA_OBJETIVO = "Comida rápida"
UMBRAL_PRECIO = 15000
DESCUENTO = 0.15


def calcular_precio_final(categoria, precio_base):
    """
    Calcula el precio final del producto.
    Aplica un descuento del 15% si el producto pertenece
    a la categoría objetivo y supera el umbral de precio.
    """

    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        descuento = precio_base * DESCUENTO
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final


print("===== MENÚ DE RESTAURANTE =====")
print("Categoría con promoción:", CATEGORIA_OBJETIVO)
print("Descuento aplicado: 15%")
print("--------------------------------")

for producto in menu:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio base: $", precio_base)
    print("Precio final: $", precio_final)
    print("--------------------------------")