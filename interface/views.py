from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from forms import CollectForm, AnaliseForm
import pdb


FILES_DIRECTORY = "C:\\"
def index(request):
	return render(request,'index.html', {'form':CollectForm(),"form_analise":AnaliseForm(directory=FILES_DIRECTORY) })

def collectTweetsForm(request):
	form = CollectForm(request.POST)
	if(form.is_valid()):
		#PEGANDO inputs da tela aqui, fazer uma logica com eles...
		hashtag_value = form.cleaned_data["hashtag"]
		duration_value = form.cleaned_data["duration"]
		max_tweets_value = form.cleaned_data["max_tweets"]
		return HttpResponse("PEGANDO OS TWEETS")
	return index(request)

def analiseTweetsForm(request):
	filename_value = request.GET["filename"]
	filepath = FILES_DIRECTORY + filename_value
	#ADICIONAR logica de leitura de arquivo e analise aqui
	
	#gerar um json pra botar no grafico
	graphic_json = "json : json"
	request.session['graphic_json'] = graphic_json
	return redirect("graphicView")

def graphic(request):
	print request.session['graphic_json']
	return render(request, "graphic.html")