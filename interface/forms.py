from django import forms
from os import listdir
import pdb


css={'class': "input-lg"}

class CollectForm(forms.Form):
	hashtag = forms.CharField(label="Hashtag", required=True, max_length=10,widget=forms.TextInput(attrs=css))
	duration = forms.IntegerField(label="Duracao", required=True, max_value=3600,min_value=1,widget=forms.NumberInput(attrs=css))
	max_tweets= forms.IntegerField(label="Max Tweets", required=True, max_value=999999999,min_value=1,widget=forms.NumberInput(attrs=css))	
	#duration = forms.DurationField(label="duration")

class AnaliseForm(forms.Form):

	def __init__(self, *args,**kwargs):
		#pdb.set_trace()
		if(kwargs.has_key('directory')):
			filename_list = listdir(kwargs.pop('directory'))
		self.formated_choices =[]
		for name in filename_list:
			self.formated_choices.append((name,name))
		super(AnaliseForm,self).__init__(*args,**kwargs)
		
		self.fields["filename"] = forms.ChoiceField(label="arquivo", choices=self.formated_choices)