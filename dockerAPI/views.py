from django.shortcuts import render, HttpResponse
from .models import Docker

# Create your views here.
def index(request):
	containerList = Docker.getContainerList()
	context = {'containerList' : containerList}
	return render(request, 'dockerAPI/index.html', context)

def images(request):
	imageList = Docker.getImageList()
	context = {'imageList' : imageList}
	return render(request, 'dockerAPI/imageList.html', context)

'''
Beispiel um Fehler zu werfen
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
'''