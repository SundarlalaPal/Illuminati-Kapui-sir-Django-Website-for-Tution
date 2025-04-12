from django.shortcuts import render, redirect
import utils_my_personal

# Create your views here.
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        age = request.POST.get("age")
        guardianname = request.POST.get("guardianname")
        phonenumber = request.POST.get("phonenumber")
        email = request.POST.get("email")
        password = request.POST.get("password")
        classs = request.POST.get("class")
        board = request.POST.get("board")
        id_token = utils_my_personal.Firebase_Operations().create_user_tem(firstname=first_name,lastname=last_name,email=email, password=password,age=age,guardianname=guardianname,phone=phonenumber,classs = classs, board=board)
        if id_token==False:
            return render(request, "authentication/signup.html", {"error": "User already exists"})
        else:
            return render(request, "authentication/signedup.html")
    if request.method == "GET":
        return render(request, "authentication/signup.html")

def login(request):
    if request.method == "GET":
        return render(request, "authentication/login.html")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        login_user_id = utils_my_personal.Firebase_Operations().login_user(email, password)
        if login_user_id:
            request.session["id_token"] = login_user_id
            return redirect("/dashboard")
        else:
            return render(request, "authentication/login.html", {"error": "Invalid credentials"})



def logout(request):
    request.session.flush()  # Clears session
    return redirect("/")
            
