import random
import string
from django.shortcuts import render

def generar_contrasena(longitud):
    if longitud < 8:
        return "La longitud de la contraseña debe ser al menos 8 caracteres."
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def index(request):
    contrasena = None
    error = None
    
    if request.method == "POST":
        try:
            longitud = int(request.POST.get("longitud", 8))
            contrasena = generar_contrasena(longitud)
        except ValueError:
            error = "Por favor, introduce un número válido."
    
    return render(request, "index.html", {"contrasena": contrasena, "error": error})
