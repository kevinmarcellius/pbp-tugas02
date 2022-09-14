from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.

def show_catalog(request):
    return render(request, "katalog.html", context)
data_katalog = CatalogItem.objects.all()
context = {
    'list_item': data_katalog,
    'name': 'Kevin Marcellius Alrino',
    'student_id': '2106706193'
}