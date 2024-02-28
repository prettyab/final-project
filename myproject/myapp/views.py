from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('Fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        department = request.POST.get('department')
        year_of_experience = request.POST.get('yearofExperience')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use.')
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.username =email
        user.save()

        messages.success(request, 'Registration successful. Please log in.')
        return redirect('user_login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email,password=password)
        if user is not None:
            auth_login(request, user)

            request.session['user_id'] = user.id
            request.session['user_email'] = user.email

            return redirect('predict_salary')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('user_login')

    return render(request, 'loggin.html')


def About(request):
    return render(request, 'About.html')
def Contact(request):
    return render(request, 'Contact.html')
def Service(request):
    return render(request, 'Service.html')

def homee(request):
    return render(request, 'homee.html')
from django.shortcuts import render
from.forms import SalaryPredictionForm
import pickle
import numpy as np
MODEL_PATH = "C:/Users/DELL/myproject/myapp/static/salary.pickle"

def make_prediction(YearsExperience):
    # Load the trained model
    model = pickle.load(open(MODEL_PATH, 'rb'))
    
    # Make a prediction using the loaded model
    prediction = model.predict([[YearsExperience]])

    return prediction[0]
def predict_salary(request):
    # Create an instance of the SalaryPredictionForm
    form = SalaryPredictionForm(request.POST or None)

    # Check if the form is submitted and valid
    if request.method == 'POST' and form.is_valid():
        # Get input values from the form
        YearsExperience = form.cleaned_data['YearsExperience']
        
        # Make a prediction using the loaded model
        prediction = make_prediction(YearsExperience)

        # Save the prediction to the database
        instance = form.save(commit=False)
        instance.Salary = prediction
        instance.save()

        # Round the prediction for display
        rounded_prediction = np.round(prediction, 2)

        # Render the results page with the rounded prediction
        return render(request, 'results.html', {'prediction': f'The predicted salary is: ${rounded_prediction}'})

    # Render the details page with the form
    return render(request, 'home2.html', {'form': form})
