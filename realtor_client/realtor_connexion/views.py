from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OdooLoginForm,OdooSignInForm
# from .models import OdooConfig
from realtor_client.rpc import connect_odoo_password,create_user

def odoo_login(request):
    if request.method == 'POST':
        form = OdooLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            url = "http://localhost:8069"
            db = "web1"

            try:
                
                # Tester la connexion
                uid,_ = connect_odoo_password(url, db, username, password)

                # Enregistrer les informations dans la session
                request.session['odoo_uid'] = uid
                request.session['odoo_username'] = username
                request.session['odoo_password'] = password
                request.session['odoo_url'] = url
                request.session['odoo_db'] = db

                
                return redirect('list_appart')  # Redirection vers le tableau de bord
            except Exception as e:
                return HttpResponse(f"Erreur : {str(e)}")
    else:
        form = OdooLoginForm()

    return render(request, 'realtor_connexion/odoo_login.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = OdooSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email=form.cleaned_data['email']
            url = "http://localhost:8069"
            db = "web1"

            try:
                create_user(url,db,username,email,password)
                # Tester la connexion        
                uid,_ = connect_odoo_password(url, db, email, password)
                # Enregistrer les informations dans la session
                request.session['odoo_uid'] = uid
                request.session['odoo_username'] = username
                request.session['odoo_password'] = password
                request.session['odoo_url'] = url
                request.session['odoo_db'] = db

                
                return redirect('list_appart')  # Redirection vers le tableau de bord
            except Exception as e:
                return HttpResponse(f"Erreur : {str(e)}")
    else:
        form = OdooSignInForm()

    return render(request, 'realtor_connexion/odoo_sign_in.html', {'form': form})
