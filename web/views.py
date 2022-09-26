import email
from django.shortcuts import render,redirect
import pyrebase

# Create your views here.


#Applyinf firebase to the project 
# // Your web app's Firebase configuration
# // For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
  "apiKey": "AIzaSyDN-Sne0GF1uSNlIYU_aRKqI7iIigAh7ww",
  "authDomain": "judicary-5d20a.firebaseapp.com",
  "databaseURL": "https://judicary-5d20a-default-rtdb.firebaseio.com",
  "projectId": "judicary-5d20a",
  "storageBucket": "judicary-5d20a.appspot.com",
  "messagingSenderId": "286397750808",
  "appId": "1:286397750808:web:536792ae3e428ba8d26d6d",
  "measurementId": "G-BMHM4XDXVY"
};

# # // Initialize Firebase

firebase = pyrebase.initialize_app(firebaseConfig)

# Get reference to the auth service

auth = firebase.auth()

def home(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            auth.sign_in_with_email_and_password(email=email,password=password)
            if password == auth.sign_in_with_email_and_password(email=email):

                return redirect('dashboard.html/')
            else:
                print("error")
        except:
            print('error')
    else:
        return render(request, 'home.html')


def dashboard(request):
        return render(request, 'dashboard.html')
