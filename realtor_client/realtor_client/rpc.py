import xmlrpc.client
#ma cle api b4ef80c93732f15bc05f99cad028da59407fe83d

# Fonction pour se connecter à Odoo
import xmlrpc.client

def connect_odoo_password(url, db, username, password):
    """Connexion à Odoo avec login/mot de passe"""
    try:
        # Récupération de la version d’Odoo
        common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
        print("Version :", common.version())

        # Connexion utilisateur
        uid = common.authenticate(db, username, password, {})
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        print(uid)
        if not uid:
            raise Exception("Échec de l'authentification.")

        # Référence aux modèles Odoo
        models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
        return uid, models
    except Exception as e:
        raise Exception(f"Erreur lors de la connexion à Odoo : {e}")
    


def create_user(url,db,name,email,password): 
    uid, models= connect_odoo_password(url, db, 'odoo', 'odoo')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     ')
    print(models)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     ')
   
    models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object") 
    partner_id = models.execute_kw(
    db, uid, 'odoo',
    'res.partner', 'create',
    [{'name': name, 'email': email}])
    
    print('cree le res.partner')
    user_id = models.execute_kw(
    db, uid, 'odoo',
    'res.users', 'create',
    [{'partner_id': partner_id, 'login': email, 'password': password}])
   
    print('cree le res.user')
  

    return user_id




#chat ma donner cette methodePCQ JE SUIS FATIGUER FELEMME ECRIRE
def connect_odoo_with_token(url, db, token):
  
    # Récupération de la version d'Odoo installée
    common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
    print("Version : ", common.version())
# L'authentification via token nécessite un UID fictif, ici `1` comme exemple
    uid = 1  # Utilisation d'un uid fictif pour l'authentification par token
    # Connexion via token API (pas besoin de UID)
    models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
    return models, uid

def find_appart_by_name(models,db,username,pasword, appart_name): 
    ids = models.execute_kw(
    db, uid, password,
    'realtor.apartment', 'search',
    [[('name', '=', appart_name)]]  # Liste contenant des tuples de conditions
    )
    print(f"IDs trouvés pour '{appart_name}' :", ids)

def list_apartments(models, db, uid, password):
    print('rentre ici')
    apartments = models.execute_kw(
        db, uid, password, 
        'realtor.apartment', 'search_read', 
        [[]], 
        {'fields': ['name', 'expected_price', 'best_offer', 'stock_quantity','photo']}
    )
    print('listteeeeeee')
    #print('Liste des appartements:', apartments)
    return apartments


def list_partner(models, db, uid, password):
    print('Récupération des partenaires...')
    partners = models.execute_kw(
        db, uid, password, 
        'res.partner', 'search_read', 
        [[('is_a_buyer', '=', True)]],  # Condition pour filtrer les partenaires acheteurs
        {'fields': ['name']}  # Champs à récupérer
    )
    print('Liste des acheteurs:', partners)
    return partners


def offer(models, db, uid, password, apartment_id, buyer_id, offer_price):
    print('Proposition d\'offre...')
    try:
        # Créer une offre
        offer_id = models.execute_kw(
            db, uid, password, 
            'realtor.offer', 'create', 
            [{
                'apartment_id': apartment_id, 
                'buyer_id': buyer_id, 
                'offer_price': offer_price
            }]
        )
        print(f'Offre créée avec succès, ID de l\'offre : {offer_id}')
        return offer_id
    except Exception as e:
        print(f'Erreur lors de la création de l\'offre : {str(e)}')
        return None

def getoffer(db, uid, password,models): 
      
     alloffer = models.execute_kw(
        db, uid, password, 
        'realtor.offer', 'search_read', 
         [[]],
        {'fields': ['apartment_id','buyer_id','offer_price']}  # Champs à récupérer
    )
     return alloffer


def getoffero(db, uid, password,models): 
      
     alloffer = models.execute_kw(
        db, uid, password, 
        'realtor.offer', 'search_read', 
         [[('offer_price','>','10000')]],
        {'fields': ['apartment_id','buyer_id','offer_price']}  # Champs à récupérer
    )
     return alloffer



#chat ma donner ce main pour tester PCQ JE SUIS FATIGUER FELEMME ECRIRE
# Exemple d'utilisation
if __name__ == "__main__":

    url = "http://localhost:8069"
    db = "web1"
    username = "odoo"
    password = "odoo"
    appart_name = "appppppaaaaart"
    token = 'b4ef80c93732f15bc05f99cad028da59407fe83d'  # Token API de naoufal
 
 #Connexion via login/mot de passe
    try:
        print("Connexion avec login et mot de passe...")
        uid, models =connect_odoo_password(url,db,username,password) 
        #connect_odoo_password(url, db, username, password)
        # find_appart_by_name(models, db, uid, password, appart_name)
        # connect_odoo_password(url,db,'mama','mama@gmail.com','mama#')
        # list_apartments(models,db,uid,password)
        alloffer=getoffero(db, uid, password,models)
        print(alloffer)
    except Exception as e:
        print("Erreur avec login/mot de passe :", e)

    # Connexion via token API
    # try:
    #     print("Connexion avec token API...")
    #     models, token_param = connect_odoo_with_token(url, db, token)
    #     find_appart_by_name(models, db, uid, password, appart_name)

    # except Exception as e:
    #     print("Erreur avec token API :", e)



# #ces deux ligne la cree un appart FAIRE DES FOCNTION??
# id_created = models.execute_kw(db, uid, password,
# 'realtor.apartment', 'create',
# [{'name': 'appppppaaaaart', 'description': 'acchete stp','availability_date':'2025-03-14 10:00:00','expected_price':'12345','surface':'123','total_surface':'345'}])
# models.execute_kw(db, uid, password,'realtor.apartment', 'unlink', [[id_created]])
