from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.files import File

from web.models import change, text

from django.template.loader import render_to_string

# Create your views here.

def html(request):
	file = open("web/templates/web/index.html", 'r')
	contents = file.read()
	file.close()
	return HttpResponse(contents, content_type='text/plain')
	

def index(request):
	context = {
	'bkg_color': str(change.objects.get(pk=1)),
	'text_list': text.objects.all(),
	'box_style': str(change.objects.get(pk=3)),

	}
	if (request.POST):
		#obtain input (text) based on name attribute
		info = request.POST.dict()


		#background-color

		bkg = info.get("color")

		if bkg: #has the user entered a new color?

			a = change.objects.get(pk=1)
			a.text = str(bkg)
			a.save()



		#text
		txt = info.get("para")

		if txt:

			new = text(text=str(txt)) #save txt to database
			new.save()

			para = change.objects.get(pk=2)
			para.text = str(txt)
			para.save()

		#BOX
		box = info.get("box")

		if box:
			style = change.objects.get(pk=3)
			style.text = str(box)
			style.save()

		#LINKS -- YOUTUBE?

		#FILES?

		#TEMPLATES
			#SHOW HTML //different pages


		return render(request, 'web/index.html', context)



	
	return render(request, 'web/index.html', context)