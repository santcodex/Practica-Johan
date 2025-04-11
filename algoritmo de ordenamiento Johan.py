import random
import tkinter as tk
from tkinter import ttk, messagebox
import time  # Para medir tiempos de ejecución
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CarFixapp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Fix - Ofertas de Repuestos")
        self.root.geometry("800x600")
        
      
        self.negocios = self.Negocios(20)
        self.productos = self.Productos(100, self.negocios)
        
        
        self.Interfaz()
    
    def Negocios(self, cantidad):
        negocios = []
        for i in range(cantidad):
            negocio = {
                'nombre': f"Negocio {i + 1}",
                'ventas': random.randint(10, 500)  # ventas concretadas
            }
            negocios.append(negocio)
        return negocios
    
    def Productos(self, cantidad, negocios):
        productos = []
        for i in range(cantidad):
            negocio_elegido = random.choice(negocios)
            producto = {
                'nombre': f"Producto {i + 1}",
                'precio': round(random.uniform(50.0, 1000.0), 2),
                'negocio': negocio_elegido['nombre']
            }
            productos.append(producto)
        return productos
    
    def quicksortProductos(self, lista):
        if len(lista) <= 1:
            return lista
        
        pivot = lista[len(lista) // 2]['precio']
        left = [producto for producto in lista if producto['precio'] < pivot]
        middle = [producto for producto in lista if producto['precio'] == pivot]
        right = [producto for producto in lista if producto['precio'] > pivot]
        return self.quicksortProductos(left) + middle + self.quicksortProductos(right)
    
    def insertionsortNegocios(self, lista):
        negocios = lista.copy()
        for i in range(1, len(negocios)):
            key = negocios[i]
            j = i - 1
            while j >= 0 and negocios[j]['ventas'] < key['ventas']:
                negocios[j + 1] = negocios[j]
                j -= 1
            negocios[j + 1] = key
        return negocios
    
    def Interfaz(self):
        frame_principal = ttk.Frame(self.root, padding="20")
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(
            frame_principal, 
            text="Car Fix - Ofertas de Repuestos", 
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(pady=10)
        
        ttk.Button(
            frame_botones,
            text="Productos Ordenados",
            command=self.mostrarProductos
        ).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(
            frame_botones,
            text="Negocios Ordenados",
            command=self.mostrarNegocios
        ).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(
            frame_botones,
            text="Comparar Algoritmos",
            command=self.compararAlgoritmos
        ).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(
            frame_botones,
            text="Información",
            command=self.mostrarInfo
        ).pack(side=tk.LEFT, padx=10)
        
        self.frame_resultados = ttk.Frame(frame_principal)
        self.frame_resultados.pack(fill=tk.BOTH, expand=True)
    
    def mostrarProductos(self):
        productos_ordenados = self.quicksortProductos(self.productos)
        mensaje = "Productos Ordenados por Precio (Ascendente):\n\n"
        for p in productos_ordenados[:10]:
            mensaje += f"Nombre: {p['nombre']}, Precio: ${p['precio']:.2f}, Negocio: {p['negocio']}\n"
        messagebox.showinfo("Productos Ordenados", mensaje)
    
    def mostrarNegocios(self):
        negocios_ordenados = self.insertionsortNegocios(self.negocios)
        mensaje = "Negocios Ordenados por Ventas (Descendente):\n\n"
        for n in negocios_ordenados:
            mensaje += f"Negocio: {n['nombre']}, Ventas: {n['ventas']}\n"
        messagebox.showinfo("Negocios Ordenados", mensaje)
    
    def compararAlgoritmos(self):
        start_quick_sort = time.time()
        self.quicksortProductos(self.productos)
        end_quick_sort = time.time()
        quick_sort_time = end_quick_sort - start_quick_sort
        
        start_insertion_sort = time.time()
        self.insertionsortNegocios(self.negocios)
        end_insertion_sort = time.time()
        insertion_sort_time = end_insertion_sort - start_insertion_sort
        
        
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(
            ["Quick Sort", "Insertion Sort"], 
            [quick_sort_time, insertion_sort_time], 
            color=["blue", "green"]
        )
        ax.set_title("Comparación de Algoritmos")
        ax.set_ylabel("Tiempo de Ejecución (s)")
        
        
        canvas = FigureCanvasTkAgg(fig, master=self.frame_resultados)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def mostrarInfo(self):
        Info = (
            "Car Fix - Aplicación de Buffer Ring\n\n"
            "Funciones:\n"
            "- Mostrar Productos Ordenados: Ordena los productos de menor a mayor precio (Quick Sort).\n"
            "- Mostrar Negocios Ordenados: Ordena los negocios de mayor a menor ventas (Insertion Sort).\n"
            "- Comparar Algoritmos: Compara el tiempo de ejecución de Quick Sort e Insertion Sort.\n"
            "- Información: Muestra esta información adicional.\n\n"
            "La aplicación brinda a los usuarios una forma rápida de comparar precios y elegir "
            "un negocio confiable basado en su experiencia de ventas."
        )
        messagebox.showinfo("Información", Info)

def main():
    root = tk.Tk()
    CarFixapp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
