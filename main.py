import os

introduccion = """""
<div class="intro-section" style="margin-top: 30px;">
    <h2>Aircraft Collection</h2>
    <p class="main-text">Now we will show the aircraft details below, including their main specifications and features. I hope this can help you and learn more about these amazing aircraft:</p>
    <hr />
</div>
"""


imagen_avion = "emb170.jpg" 
for archivo in os.listdir("."):
    if archivo.lower().startswith("emb170"):
        imagen_avion = archivo
        break

print(f"¡Imagen encontrada y lista para usar: {imagen_avion}!")

# Definimos el avión usando la imagen detectada
aviones = [
    {
        "nombre": "Embraer 170",
        "imagen": imagen_avion,
        "descripcion": "A short-to-medium range twin-engine regional jet widely used by airlines worldwide for connecting smaller hubs."
    }
]

# 3. Leemos el index.html actual
with open("index.html", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

# 4. Limpiamos cualquier bloque anterior generado por Python para evitar duplicados
if '<div class="aviapedia-dinamico">' in contenido:
    partes = contenido.split('<div class="aviapedia-dinamico">')
    contenido = partes[0] + "</main>"

# 5. Construimos el nuevo bloque limpio y ordenado
bloque_nuevo = '\n<div class="aviapedia-dinamico">\n'
bloque_nuevo += introduccion

bloque_nuevo += "<div class='aviones-container'>\n"
for avion in aviones:
    bloque_nuevo += f"""
    <div class="avion-card">
        <h2>{avion['nombre']}</h2>
        <img src="{avion['imagen']}" alt="{avion['nombre']}" width="1" />
        <p class="main-text">{avion['descripcion']}</p>
        <hr />
    </div>
    """
bloque_nuevo += "</div>\n"
bloque_nuevo += "</div>\n"

# 6. Insertamos justo después de la palabra 'expanding.'
punto_de_insercion = "expanding."
if punto_de_insercion in contenido:
    contenido_nuevo = contenido.replace(punto_de_insercion, punto_de_insercion + bloque_nuevo)
else:
    contenido_nuevo = contenido.replace("</main>", bloque_nuevo + "</main>")

# 7. Guardamos los cambios
with open("index.html", "w", encoding="utf-8") as archivo:
    archivo.write(contenido_nuevo)

print("¡Listo! Página actualizada con éxito y la imagen ya debería verse.")