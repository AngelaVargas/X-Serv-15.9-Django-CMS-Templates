from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.

@csrf_exempt
def index(request, peticion):

	if request.method == "POST":
		p = Pages(name=request.POST['nombre'], page=request.POST['descripcion'])
		p.save()

	try:
		Request = Pages.objects.get(name=peticion)
		template = get_template("Simple_Beauty/index.html")
		c = Context({'title': Request.name, 'content': Request.page})
		renderizado = template.render(c)
		return HttpResponse(renderizado)

	except Pages.DoesNotExist:
		Response = "Este recurso no está en la base de datos. Introduce su valor y descripción."
		Response += '<form action="" method="POST">' + '<br>'
		Response += 'Valor: <input type="text" name="nombre">' +  '<br>'
		Response += 'Descripción: <input type="text" name="descripcion">' + '<br>' 
		Response += '<br>' + '<input type="submit" value="Enviar">'
		return HttpResponse(Response)
