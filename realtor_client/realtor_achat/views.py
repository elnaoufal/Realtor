from django.shortcuts import render, redirect
from realtor_client.rpc import connect_odoo_password, list_apartments, list_partner, offer
from django.http import HttpResponse
import xmlrpc.client
def list_apartments_view(request):
    try:
        # Récupérer les informations de connexion à partir de la session
        url = request.session['odoo_url']
        db = request.session['odoo_db']
        username = request.session['odoo_username']
        password = request.session['odoo_password']
        uid = request.session['odoo_uid']

        # Recréer l'objet models
        models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object") 

        # Obtenir la liste des appartements
        apartments = list_apartments(models, db, uid, password)
        
        #obtenir les res.partner 
        partners = list_partner(models, db, uid, password)

        # Renvoyer les appartements à la vue
        return render(request, 'realtor_achat/list_appartement.html', {'apartments': apartments, 'partners' : partners, 'username' : username, 'uid' : uid})

    except KeyError as e:
        return HttpResponse(f"Erreur : clé manquante dans la session ({str(e)})", status=400)
    except Exception as e:
        return HttpResponse(f"Erreur : {str(e)}", status=500)
    
    
def propose_offer(request):
    if request.method == 'POST':
        try:
            # Récupérer les informations de connexion
            url = request.session['odoo_url']
            db = request.session['odoo_db']
            username = request.session['odoo_username']
            password = request.session['odoo_password']
            uid = request.session['odoo_uid']

            # Recréer l'objet models
            models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

            # Récupérer les données du formulaire
            apartment_id = int(request.POST['apartment_id'])
            buyer_id = uid
            offer_price = float(request.POST['offer_price'])

            # Proposer l'offre
            offer_id = offer(models, db, uid, password, apartment_id, buyer_id, offer_price)

            if offer_id:
                return HttpResponse(f"Offre créée avec succès (ID : {offer_id})", status=200)
            else:
                return HttpResponse("Erreur lors de la création de l'offre", status=500)
        except Exception as e:
            return HttpResponse(f"Erreur : {str(e)}", status=500)
    return HttpResponse("Méthode non autorisée", status=405)

    
