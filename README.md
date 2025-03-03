# Realtor
This project is a real estate management system developed with Odoo and Django.  It enables the management of apartments, stock, and sales offers through API synchronization.

## Features  

### Odoo Module (Realtor)
- Manage apartments (add, update, delete, display).  
- Stock management via Odoo Stock module.  
- Synchronization of real estate data with external applications.  

### Django Client (Realtor-Client)
- Interface for real estate developers.  
- Display available apartments for sale.  
- Offer submission system for buyers.  
- Synchronization of offers with Odoo via XML-RPC.  

## Technologies Used  
- **Backend**: Odoo (Python), Django (Python)  
- **Database**: PostgreSQL (Odoo), SQLite/MySQL (Django)  
- **API**: XML-RPC for integration with Odoo  

## Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/elnaoufal/realtor.git
cd realtor
```
### 2. Intsall Odoo 
https://www.odoo.com/documentation/17.0/administration/on_premise/packages.html
### 3. Install django dependencies
#### Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
#### Install Django:
```bash
pip install django
```
#### Apply migrations:
```bash
python manage.py migrate
```
#### Run the development server:
```bash
python manage.py runserver
```
After starting the server, visit http://127.0.0.1:8000/ in your browser to access the application

# Using Docker 
## 1. Start the PostgreSQL container:
```bash
docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres -p 5433:5432 --name db postgres:17
```
## 2. Start the Odoo container with addons:
```bash
docker run -v [your path]\addons:/mnt/extra-addons -p 8069:8069 --name odoo --link db:db -t odoo:17 --dev=all
```
After starting the server, visit http://127.0.0.1:8069 in your browser to access the application odoo
