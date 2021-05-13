from django.shortcuts import render, render_to_response
import os

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def modelview(request):
    path="./media/models"
    model_list = os.listdir(path)
    model_list.sort()
    return render_to_response('main/model_view.html', {'list': model_list})