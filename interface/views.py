from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from forms import CollectForm, AnaliseForm
from logger import *
from subprocess import call
import os
import pdb

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
FILES_DIRECTORY = os.path.join(PROJECT_ROOT, 'arquivos/')
def index(request):
	return render(request,'index.html', {'form':CollectForm(),"form_analise":AnaliseForm(directory=FILES_DIRECTORY) })

def collectTweetsForm(request):
	form = CollectForm(request.POST)
	if(form.is_valid()):
		hashtag_value = form.cleaned_data["hashtag"]
		duration_value = form.cleaned_data["duration"]
		max_tweets_value = form.cleaned_data["max_tweets"]
			
		twitter_stream = Stream(auth, MyListener(fname=hashtag_value+".txt", time_limit=duration_value, tweets_limit=max_tweets_value))
		twitter_stream.filter(track=["#"+hashtag_value])
		
		return HttpResponse("PEGANDO OS TWEETS")
	return index(request)

def analiseTweetsForm(request):
	filename_value = request.GET["filename"]
	filepath = FILES_DIRECTORY + filename_value
	#ADICIONAR logica de leitura de arquivo e analise aqui
	call("spark-submit %s %s" % ( os.path.join(FILES_DIRECTORY, "analise.py") ,filename_value), shell=True)
	#gerar um json pra botar no grafico
	graphic_json = "json : json"
	request.session['graphic_json'] = graphic_json
	return redirect("graphicView")

def graphic(request):
	print request.session['graphic_json']
	return render(request, "graphic.html")