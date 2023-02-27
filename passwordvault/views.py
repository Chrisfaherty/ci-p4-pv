from django.shortcuts import render


def page_not_found_400_view(request, exception):
    return render(request, '400.html', status=400)

def page_not_found_404_view(request, exception):
    return render(request, '404.html', status=404)

def page_not_found_500_view(request, exception):
    return render(request, '500.html', status=500)