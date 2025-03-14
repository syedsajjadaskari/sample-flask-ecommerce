# E-Commerce Website

Simple e-commerce website built with Flask and SQLite. Allows users to register, login, and purchase items. Also has an admin panel that allows administrators to view and manage users and items.

## Dependencies
```
bcrypt==4.3.0
blinker==1.9.0
click==8.1.8
Flask==3.1.0
Flask-Bcrypt==1.0.1
Flask-Login==0.6.3
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
greenlet==3.1.1
gunicorn==23.0.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
packaging==24.2
SQLAlchemy==2.0.38
typing_extensions==4.12.2
Werkzeug==3.1.3
WTForms==3.2.1
```

## Installation
1. Clone the repository.
   ```bash
      https://github.com/syedsajjadaskari/sample-flask-ecommerce.git
   ```
2. Install the dependencies.
   ```bash
   pip install -r requirements.txt
   ```
3. Create a database.
   ```bash
   sudo apt install sqlite3
   sqlite3 e-commerce.db
   ```
   to exit from the sqlite 3
   ```
   .exit
   ```
4. Create the tables.
   ```sql
   CREATE TABLE users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT UNIQUE NOT NULL,
       email_address TEXT UNIQUE NOT NULL,
       password_hash TEXT NOT NULL,
       budget INTEGER NOT NULL DEFAULT 10000
   );
   
   CREATE TABLE items (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT UNIQUE NOT NULL,
       barcode TEXT UNIQUE NOT NULL,
       price INTEGER NOT NULL,
       description TEXT NOT NULL,
       owner INTEGER REFERENCES users (id)
   );
   ```
5. Run the website.
   ```
   which gunicorn
   #copy the path
   path="what ever copy path paste it" 
   //make sure there is no space for example path=/home/azureuser/sample-flask-ecommerce/venv/bin/gunicorn
   sudo env PATH=$PATH gunicorn --bind 0.0.0.0:80 Market:app

   ```

## Usage
- Register for an account.
- Login to your account.
- Browse the items for sale.
- Add items to your cart.
- Checkout and pay for your items.

## Admin Panel
The admin panel allows administrators to view and manage users and items. It also has two tabs: "Control Users" and "Control Items" to easily view and manage.

**Username:** admin  
**Password:** admin  



## License
This project is licensed under the MIT License - see the LICENSE file for details.

