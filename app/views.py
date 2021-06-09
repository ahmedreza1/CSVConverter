from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import tabula,random
# Create your views here.
def index(request): 
    output = ""
    output_file_name=""
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(f'pdf/{myfile.name}', myfile)
        uploaded_file_url = fs.url(filename)
        output_file_name=str(random.randint(0, 99999))
        output = f"media/csv_list/{output_file_name}.csv"
        tabula.convert_into(settings.MEDIA_ROOT+"/"+filename, output, output_format="csv",pages="all")

    return render(request, "index.html", {"output":output,'output_file_name':output_file_name})
