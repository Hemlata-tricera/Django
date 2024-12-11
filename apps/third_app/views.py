from django.shortcuts import render, redirect
from .models import Student
# from django.http import HttpResponse
from django.contrib import messages




# Create your views here.
def student_detail(request):
    # return HttpResponse("I am on student Page")
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})
#
def add_student(request):
    if request.method == 'POST':
        action = request.POST.get('action')  # Get the action (add or delete)

        # Handle Deletion
        if action == 'delete':
            roll_no = request.POST.get('rollno')  # Get the roll number for deletion

            try:
                # Try to find the student and delete them
                student = Student.objects.get(rollno=roll_no)
                student.delete()  # Delete the student record
                messages.success(request, f'Student with roll number {roll_no} has been deleted.')
            except Student.DoesNotExist:
                messages.error(request, f'No student found with roll number {roll_no}.')

            return redirect('all_students')  # Redirect after deletion

        # Handle Addition of Student
        else:
            # Gather form data
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            roll_no = request.POST.get('rollno')
            email = request.POST.get('email')
            gender = request.POST.get('gender')

            if fname and lname and roll_no and email and gender:
                # Create a new student if all fields are provided
                create_status = Student.objects.create(
                    fname=fname,
                    lname=lname,
                    dob='2024-12-10',  # Use dynamic date if necessary
                    rollno=roll_no,
                    email=email,
                    gender=gender
                )

                if create_status:
                    messages.success(request, f'Student {fname} {lname} added successfully!')
                    return redirect('all_students')  # Redirect after adding student
            else:
                messages.error(request, 'Please fill in all required fields.')

    # If not a POST request, render the form
    return render(request, 'create_stud.html')

