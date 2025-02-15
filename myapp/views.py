from django.shortcuts import render

def testing_view(request):
    return render(request, 'testing.html')  # This will render an HTML file
