from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Student
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from django.urls import reverse






# Create your views here.
def student_detail(request):
    # import pdb
    # pdb.set_trace()
    # return HttpResponse("I am on student Page")
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})
#
def add_student(request):
    # import pdb
    # pdb.set_trace()
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
            gender = request.POST.get('gender', 'male')

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

def update(request, rollno):
    try:
        student = Student.objects.get(rollno=rollno)  # Retrieve the student by rollno
    except Student.DoesNotExist:
        # Handle the case where the student does not exist
        messages.error(request, f"Student with roll number {rollno} does not exist.")
        return redirect('all_students')  # Redirect to all students page if not found

    # Render the update form with the student details
    return render(request, 'update.html', {'student': student})

# def updaterecord(request, id):
#   first = request.POST['fname']
#   last = request.POST['lname']
#
#   student = Student.objects.get(rollno=id)
#   student.firstname = first
#   student.lastname = last
#   student.save()
#   return HttpResponseRedirect(reverse('stud'))

def updaterecord(request, rollno):
    if request.method == 'POST':
        # Get form data from the POST request
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        gender = request.POST.get('gender', 'male')

        try:
            # Get the student to be updated
            student = Student.objects.get(rollno=rollno)

            # Update student details
            student.fname = fname
            student.lname = lname
            student.email = email
            student.gender = gender
            student.save()  # Save the updated student record

            messages.success(request, f'Student {fname} {lname} updated successfully!')
            return redirect('all_students')  # Redirect after successful update

        except Student.DoesNotExist:
            messages.error(request, f'Student with roll number {rollno} not found.')
            return redirect('all_students')  # Redirect if student not found

    return HttpResponse("Invalid request method.", status=405)