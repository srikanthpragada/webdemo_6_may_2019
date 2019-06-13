from django.shortcuts import render


def add_job(request):
    if request.method == "GET":
        return render(request, 'add_job.html')
    else:  # POST request
        title = request.POST["title"]
        minsal = request.POST["minsal"]
        maxsal = request.POST["maxsal"]
        print(title, minsal, maxsal)
        # insert into JOBS table

        return render(request, "add_job.html",
                      {'msg': "Job has been added successfully!"})
