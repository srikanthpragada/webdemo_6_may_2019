import sqlite3

from django.shortcuts import render, redirect
from .forms import AddJobForm


def list_jobs(request):
    con = sqlite3.connect(r"e:\classroom\python\may6\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs")
    jobs = cur.fetchall()
    cur.close()
    con.close()
    return render(request, "list_jobs.html", {"jobs": jobs})


def add_job(request):
    if request.method == "GET":
        return render(request, 'add_job.html')
    else:  # POST request
        title = request.POST["title"]
        minsal = request.POST["minsal"]
        maxsal = request.POST["maxsal"]
        print(title, minsal, maxsal)
        # insert into JOBS table
        con = sqlite3.connect(r"e:\classroom\python\may6\hr.db")
        cur = con.cursor()
        cur.execute("insert into jobs (title,minsal,maxsal) values(?,?,?)",
                    (title, minsal, maxsal))

        if cur.rowcount == 1:
            con.commit()
            return redirect("/hr/listjobs")

        return render(request, "add_job.html",
                      {'msg': "Sorry! Could not add job!"})


def add_job_with_form(request):
    if request.method == "GET":
        f = AddJobForm()
        return render(request, 'add_job_form.html',{"form" : f})
    else:  # POST request
        f = AddJobForm(request.POST)
        if f.is_valid():
            title = f.cleaned_data['title']
            minsal = f.cleaned_data['minsal']
            maxsal = f.cleaned_data['maxsal']

            con = sqlite3.connect(r"e:\classroom\python\may6\hr.db")
            cur = con.cursor()
            cur.execute("insert into jobs (title,minsal,maxsal) values(?,?,?)",
                        (title, minsal, maxsal))

            if cur.rowcount == 1:
                con.commit()
                return redirect("/hr/listjobs")

        return render(request, "add_job_form.html",
                          {"form": f,
                           'msg': "Sorry! Could not add job!"})

