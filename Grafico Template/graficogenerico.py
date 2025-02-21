import matplotlib.pyplot as plt

# Datos
productos = ['Marcadores', 'Borradores', 'Internet', 'Papel secamanos', 'Sacos industriales',
             'Bolsas de basura pequeñas', 'Papel WC industrial', 'Papel secamanos mecha',
             'Jabón manos 5L', 'Papel A4 80g']
precios = [34.364, 56.36, 50, 220.83, 36.54, 41.02, 310.61, 110.41, 30.86, 132.374]
cantidades = [40, 7, 1, 10, 20, 30, 10, 5, 3, 20]

# Gráfico de precios
plt.figure(figsize=(10, 6))
plt.bar(productos, precios, color='blue')
plt.xlabel('Productos')
plt.ylabel('Precio (€)')
plt.title('Precios de Productos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.savefig('grafico_precios.png')  # Guarda el gráfico como una imagen
plt.close()  # Cierra la figura para liberar memoria

# Gráfico de cantidades
plt.figure(figsize=(10, 6))
plt.bar(productos, cantidades, color='green')
plt.xlabel('Productos')
plt.ylabel('Cantidad')
plt.title('Cantidades de Productos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  # Ajusta el layout para que no se corten las etiquetas
plt.savefig('grafico_cantidades.png')  # Guarda el gráfico como una imagen
plt.close()  # Cierra la figura para liberar memoria