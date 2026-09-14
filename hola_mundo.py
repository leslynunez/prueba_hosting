"""
App mínima de prueba — para verificar en minutos si un hosting
candidato es alcanzable desde Cuba (datos móviles incluidos),
antes de invertir tiempo subiendo el proyecto completo.

No tiene base de datos, no tiene dependencias más allá de Flask
mismo — el objetivo es que subir esto tome 2 minutos, no 20.

Cómo usarla (los detalles exactos de "cómo subir un archivo"
cambian según el hosting, pero la idea es siempre la misma):
    1. Crea la cuenta gratuita en el hosting candidato.
    2. Sube SOLO este archivo (hola_mundo.py) más un
       requirements.txt de una sola línea: Flask
    3. Configúralo como su punto de entrada Flask (varía por
       hosting — alwaysdata usa un WSGI parecido a PythonAnywhere).
    4. Visita la URL que te den, DESDE TU CELULAR CON DATOS
       MÓVILES (no wifi) — esa es la prueba real que importa.
    5. Si carga "Funciona..." -> este hosting SÍ es alcanzable,
       vale la pena migrar el proyecto completo.
       Si da 451 o no carga -> descarta este hosting y prueba
       el siguiente candidato, sin perder más tiempo.
"""

from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.get("/")
def hola_mundo():
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
    <body style="font-family: sans-serif; text-align: center; padding: 60px;">
        <h1>✅ Funciona — {ahora}</h1>
        <p>Si estás viendo esto desde datos móviles en Cuba, este hosting SÍ es alcanzable.</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
