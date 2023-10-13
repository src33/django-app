from django.shortcuts import render
import zipfile
import tempfile
from django.http import FileResponse
import os
import json


# Create your views here.

from . import scrape
from . import translator

def index(request):
    context={}
    return(render(request,"webtrans/index.html",context))

def test(request):

    if request.method == 'POST':
        url = request.POST['url']
        lang=request.POST['lang_list'].split(',')
        tag=request.POST['tag_list'].split(',')
        div=request.POST['div_list'].split(',')
        flpth = scrape.webtrans(url,lang,tag,div)
    # return render(request,"webtrans/index.html")
        temp_dir = tempfile.TemporaryDirectory()  # Create a temporary directory
        archive_path = os.path.join(temp_dir.name, 'archive.zip')  # Path to the archive file
        with zipfile.ZipFile(archive_path, 'w') as zipf:
            for file_path in flpth:
                file_name = os.path.basename(file_path)  # Extract the file name from the path
                zipf.write(file_path, file_name)  # Add the file to the ZIP archive

        response = FileResponse(open(archive_path, 'rb'), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="archive.zip"'
        

    # Close the temporary directory and delete it
        return response


