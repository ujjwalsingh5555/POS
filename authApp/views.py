from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from .models import Role, signup
from django.contrib import messages
from django.contrib.auth.hashers import check_password


# Create your views here.
# =========================
        # LOGIN VIEW
        # =========================
def login(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        selected_role = request.POST.get('role')
        user = signup.objects.filter(mobile_no=mobile).first()
        # Mobile check
        if not user:
            messages.error(request, "Invalid mobile number")
            return redirect('/login')
        # Active check
        if not user.is_active:
            messages.error(request, "Your account is inactive. Please contact admin")
            return redirect('/login')
        # Password check
        if not check_password(password, user.password):
            messages.error(request, "Invalid password")
            return redirect('/login')

        # Role check
        if str(user.role.id) != str(selected_role):
            messages.error(request, "Invalid role selection")
            return redirect('/login')

        # Session create
        request.session['user_id'] = user.id

        messages.success(request, "Login successful")
        return redirect('/dashboard')

    return render(request, 'Login.html')

        

    
    return render(request, 'Login.html')
 # =========================
        # STAFF CREATE VIEW
        # =========================
def staff_create(request):
    roles= Role.objects.filter(is_active=True)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile_no')
        password = request.POST.get('password')
        role = request.POST.get('role')
        is_active = request.POST.get('is_active') == 'on'
        # =========================
        # FIELD VALIDATION
        # =========================
        if not name:
            messages.error(request, "Please fill name")
            return redirect('/staff')
        if not email:
            messages.error(request, "Please fill email")
            return redirect('/staff')
        if not mobile:
            messages.error(request, "Please fill mobile number")
            return redirect('/staff')
        if not password:
            messages.error(request, "Please fill password")
            return redirect('/staff')
        if not role:
            messages.error(request, "Please select role")
            return redirect('/staff')
        # =========================
        # DUPLICATE CHECK
        # =========================
        if signup.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('/staff')
        if signup.objects.filter(mobile_no=mobile).exists():
            messages.error(request, "Mobile number already exists")
            return redirect('/staff')
        # =========================
        # ROLE FETCH
        # =========================
        role_instance = Role.objects.filter(id=role).first()
        if not role_instance:
            messages.error(request, "Invalid role selected")
            return redirect('/staff')
        # =========================
        # PASSWORD HASHING
        # =========================
        hashed_password = make_password(123)
        print(hashed_password)
        # =========================
        # CREATE STAFF
        # =========================
        signup.objects.create(
            name=name,
            email=email,
            mobile_no=mobile,
            password=hashed_password,
            role=role_instance,
            is_active=is_active
        )
        messages.success(request, "Staff created successfully")
        return redirect('/staff')
    return render(request, 'staff_create.html',{'roles':roles})



