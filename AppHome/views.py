from django.shortcuts import render
import os
from django.http import FileResponse
from django.conf import settings

# Create your views here.
def pageHome(request):
    return render(request,"pages/index.html")

def dowload_cv(request):
    file_path = os.path.join(settings.STATICFILES_DIRS[0],'pdf','CVH.pdf')
    return FileResponse(open(file_path, 'rb'),content_type='static/pdf',as_attachment=True, filename='pdf/CVH.pdf')