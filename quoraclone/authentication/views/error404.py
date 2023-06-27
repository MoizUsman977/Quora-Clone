from django.shortcuts import render

def error_404(request, exception, template_name="404.html"):
    return render(request, template_name, status=404)