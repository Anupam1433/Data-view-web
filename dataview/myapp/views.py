from django.shortcuts import render


from .models import Company


def show_data(request):
    data = Company.objects.all()
    return render(request, 'myapp/data.html', {'data': data})
