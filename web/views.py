from django.shortcuts import render
import pyrebase

# Create your views here.


#Applyinf firebase to the project 
# // Your web app's Firebase configuration
# // For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
  "apiKey": "AIzaSyDN-Sne0GF1uSNlIYU_aRKqI7iIigAh7ww",
  "authDomain": "judicary-5d20a.firebaseapp.com",
  "projectId": "judicary-5d20a",
  "storageBucket": "judicary-5d20a.appspot.com",
  "messagingSenderId": "286397750808",
  "appId": "1:286397750808:web:536792ae3e428ba8d26d6d",
  "measurementId": "G-BMHM4XDXVY"
};

# # // Initialize Firebase


def home(request):
    return render(request, 'home.html')
