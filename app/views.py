from django.shortcuts import render
from app.data_source import get_inflation_data

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {
        "inf_data": get_inflation_data()
    }

    return render(request, template_name,
                  context)