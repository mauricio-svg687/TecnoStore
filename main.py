# TecnoStore
import tkinter as tk
from tkinter import messagebox



class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        return f"{self.codigo} | {self.nombre} | S/ {self.precio} | Stock: {self.stock}"

    def calcular_valor(self):
        return self.precio * self.stock



productos = [
    Producto("P001", "Laptop Lenovo", 2500, 10),
    Producto("P002", "Mouse Logitech", 80, 25),
    Producto("P003", "Teclado Logitech", 120, 15),
    Producto("P004", "Monitor LG", 850, 8),
    Producto("P005", "Disco SSD", 350, 12),
]



def buscar_producto(codigo):
    for producto in productos:
        if producto.codigo == codigo:
            return producto
    return None


def calcular_inventario():
    total = 0
    for producto in productos:
        total = total + producto.calcular_valor()
    return total


def escribir(texto):
    """Muestra un texto en el cuadro de resultados."""
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, texto)



def registrar_producto():
    codigo = entry_codigo.get().strip().upper()
    nombre = entry_nombre.get().strip()
    if codigo == "" or nombre == "":
        messagebox.showerror("Error", "Código y nombre no pueden estar vacíos")
        return
    if buscar_producto(codigo):
        messagebox.showerror("Error", "Ese código ya existe")
        return
    try:
        precio = float(entry_precio.get())
        stock = int(entry_stock.get())
        if precio <= 0 or stock < 0:
            messagebox.showerror("Error", "Precio y stock deben ser positivos")
            return
        productos.append(Producto(codigo, nombre, precio, stock))
        mensaje = "Producto registrado correctamente"
        if stock <= 10:
            mensaje = mensaje + "\n(Producto con poco stock)"
        escribir(mensaje)
        for entrada in (entry_codigo, entry_nombre, entry_precio, entry_stock):
            entrada.delete(0, tk.END)
    except ValueError:
        escribir("Error: ingrese valores numéricos válidos")
        messagebox.showerror("Error", "Error: ingrese valores numéricos válidos")


def mostrar_productos(): 
    texto = ""
    for producto in productos:
        texto = texto + producto.mostrar() + "\n"
    escribir(texto)


def buscar_por_codigo():
    producto = buscar_producto(entry_codigo.get().strip().upper())
    if producto:
        escribir(producto.mostrar())
    else:
        escribir("Producto no encontrado")


def mostrar_inventario():
    escribir("Valor total del inventario: S/ " + str(calcular_inventario()))


def productos_poco_stock():
    texto = "Productos con poco stock:\n"
    for producto in productos:
        if producto.stock <= 10:
            texto = texto + producto.nombre + "\n"
    escribir(texto)


def precio_mayor_500():
    caros = list(filter(lambda producto: producto.precio > 500, productos))
    texto = "Productos con precio mayor a 500:\n"
    for producto in caros:
        texto = texto + producto.mostrar() + "\n"
    escribir(texto)


def salir():  
    ventana.destroy()


def mostrar_nombres(): 
    nombres = list(map(lambda producto: producto.nombre, productos))
    escribir("Nombres de productos:\n" + "\n".join(nombres))


def contar_productos(): 
    escribir("Cantidad de productos: " + str(len(productos)))


def buscar_por_nombre():  
    texto_buscado = entry_nombre.get().strip().lower()
    encontrados = list(filter(lambda p: texto_buscado in p.nombre.lower(), productos))
    if texto_buscado == "" or len(encontrados) == 0:
        escribir("Producto no encontrado")
    else:
        texto = ""
        for producto in encontrados:
            texto = texto + producto.mostrar() + "\n"
        escribir(texto)




ventana = tk.Tk()
ventana.title("TecnoStore - Gestión de Productos")

tk.Label(ventana, text="GESTIÓN DE PRODUCTOS", font=("Arial", 14, "bold")).grid(
    row=0, column=0, columnspan=2, pady=10)

# Campos de entrada
tk.Label(ventana, text="Código:").grid(row=1, column=0, sticky="e")
entry_codigo = tk.Entry(ventana)
entry_codigo.grid(row=1, column=1, pady=2)

tk.Label(ventana, text="Nombre:").grid(row=2, column=0, sticky="e")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=2, column=1, pady=2)

tk.Label(ventana, text="Precio:").grid(row=3, column=0, sticky="e")
entry_precio = tk.Entry(ventana)
entry_precio.grid(row=3, column=1, pady=2)

tk.Label(ventana, text="Stock:").grid(row=4, column=0, sticky="e")
entry_stock = tk.Entry(ventana)
entry_stock.grid(row=4, column=1, pady=2)

# Botones (cada botón ejecuta una función al hacer clic)
botones = [
    ("1. Registrar producto", registrar_producto),
    ("2. Mostrar productos", mostrar_productos),
    ("3. Buscar producto", buscar_por_codigo),
    ("4. Calcular inventario", mostrar_inventario),
    ("5. Productos con poco stock", productos_poco_stock),
    ("6. Productos con precio mayor a 500", precio_mayor_500),
    ("7. Salir", salir),
    ("8. Mostrar nombres de productos", mostrar_nombres),
    ("9. Contar productos", contar_productos),
    ("10. Buscar producto por nombre", buscar_por_nombre),
]

fila = 5
for texto, funcion in botones:
    tk.Button(ventana, text=texto, width=35, command=funcion).grid(
        row=fila, column=0, columnspan=2, pady=1)
    fila = fila + 1

# Cuadro de resultados
resultado = tk.Text(ventana, width=55, height=10)
resultado.grid(row=fila, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
