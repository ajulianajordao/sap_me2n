import tkinter as tk
from tkinter import ttk

def extrair_dados():
    # Obter valores dos widgets
    grupo_compras = grupo_compras_entry.get()
    data_documento = data_documento_entry.get()
    planta = planta_entry.get()

    # Chamar o backend de automação SAP aqui com os valores obtidos

    # Exemplo de como você pode usar os valores
    print(f"Grupo de Compras: {grupo_compras}")
    print(f"Data do Documento: {data_documento}")
    print(f"Planta: {planta}")

# Criar janela principal
root = tk.Tk()
root.title("Extração de Dados SAP")

# Criar e posicionar os widgets
grupo_compras_label = ttk.Label(root, text="Grupo de Compras:")
grupo_compras_entry = ttk.Entry(root)

data_documento_label = ttk.Label(root, text="Data do Documento:")
data_documento_entry = ttk.Entry(root)

planta_label = ttk.Label(root, text="Planta:")
planta_entry = ttk.Entry(root)

extrair_button = ttk.Button(root, text="Extrair Dados", command=extrair_dados)

# Posicionar widgets na grade
grupo_compras_label.grid(row=0, column=0, padx=5, pady=5, sticky="E")
grupo_compras_entry.grid(row=0, column=1, padx=5, pady=5)

data_documento_label.grid(row=1, column=0, padx=5, pady=5, sticky="E")
data_documento_entry.grid(row=1, column=1, padx=5, pady=5)

planta_label.grid(row=2, column=0, padx=5, pady=5, sticky="E")
planta_entry.grid(row=2, column=1, padx=5, pady=5)

extrair_button.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
