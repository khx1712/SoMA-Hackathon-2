from django.shortcuts import render, render_to_response
import os 

# Create your views here.
def index(request):
    path="./media/models" 
    model_list = os.listdir(path)
    model_list.sort()
    return render_to_response('main/index.html', {'list': model_list})