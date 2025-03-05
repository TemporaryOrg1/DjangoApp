from django.shortcuts import render

def testing_view(request):
    return render(request, "testing.html")  # This will render an HTML file

def tic_tac_toe_view(request):
    return render(request, "tic_tac_toe.html")