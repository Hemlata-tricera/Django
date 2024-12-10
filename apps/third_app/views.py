from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse



# Create your views here.
def student_detail(request):
    # return HttpResponse("I am on student Page")
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})
#
def add_student(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        # dob = request.POST.get('dob')
        roll_no = request.POST.get('rollno')
        email = request.POST.get('email')
        gender = request.POST.get('gender')

        print(fname, lname, roll_no, email, gender)
        create_status= Student.objects.create(
            fname = fname,
            lname = lname,
            dob = '2024-12-10',
            rollno = roll_no,
            email = email,
            gender = gender
        )
        if create_status:
            return redirect('all_students')
    return render(request, 'create_stud.html')