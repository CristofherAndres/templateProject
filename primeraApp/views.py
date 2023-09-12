from django.shortcuts import render

# Create your views here.
def llamarTemplate(request):
    return render(request,'primeraApp/primerTemplate.html')

def infoUsuario(request):
    data = {
        'nombre': 'Luciano',
        'apellido': 'Ramirez',
        'correo': 'luciano.ramirez@talca.cl',
        'direccion': 'Talca, Calle Barroso 123'
    }
    return render(request,'primeraApp/infoUsuario.html',data)