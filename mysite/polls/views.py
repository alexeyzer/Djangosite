from django.shortcuts import render
from .models import Mark, Model

def main(request):
    mark = Mark.objects.all()
    return render(request, 'polls/index.html', {'mark': mark})
def models(request):
    id = request.GET["id"]
    mark = Mark.objects.get(id=id)
    model = Model.objects.filter(mark=mark)
    if model is None:
        print("none")
    return render(request, 'polls/model.html', {'models': model})

