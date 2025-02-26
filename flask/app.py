from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
import mysql.connector


app = Flask(__name__)
app.secret_key = 'tourism_directory'

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/citing')
def citing():
    sites = [
        {
            'h3': 'Cameroon Wildlife Sanctuary',
            'src': 'https://th.bing.com/th?id=OLC.O68LFm1CMNRzOg480x360&w=186&h=140&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2',
            'p': "A beautiful sanctuary that offers a close encounter with Cameroon's diverse wildlife."
        },
        {
            'h3': 'Kribi Beach Resort',
            'src': 'https://bing.com/th?asid=432345564512219874&id=OAUMA.F2F177B5E000C96EBAEE9C5E37509F32_6E224B1B23B99A05&pid=21.1&o=5&w=296&h=222&rs=2&qlt=100',
            'p': 'Experience the clean, sandy beaches of Kribi, perfect for a relaxing vacation.'
        },
        {
            'h3': 'Mount Cameroon',
            'src': 'https://th.bing.com/th?id=OLC.HV3WQRT52692tw480x360&w=186&h=140&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2',
            'p': 'Take an adventurous hike up the tallest mountain in West Africa.'
        }
    ]

    return render_template('publicListing.html', listing=sites)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        name = request.form.get('title')
        description = request.form.get('description')
        phone_number = request.form.get('number')
        email = request.form.get('email')
        image = request.files.get('picture')
    #     listings = []

        if image:
            file_path = os.path.join('static', image.filename)
            image.save(file_path)

    #         listing = {
    #             'name': name,
    #             'description': description,
    #             'phone_number': phone_number,
    #             'email': email,
    #             'image': file_path
    #         }

    #         listings.append(listing)

    #         with open('listings.json', 'w') as f:
    #             json.dump(listings, f)

    #         return render_template('success_page.html',listing=listing)
    
   
conn = mysql.connector.connect(
    host="localhost", 
    user="ryan_inspires", 
    password="Asherinyuy24",
    database="wed_directory_listings_db"
    )
cursor= conn.cursor()

    

    # return redirect(url_for('index'))


@app.route('/save_to_db', methods=['GET', 'POST'])
def save_to_db():
    if request.method == 'POST':
        name = request.form.get('title')
        description = request.form.get('description')
        phone_number = request.form.get('number')
        email = request.form.get('email')
        image = request.files.get('image')
        location = request.form.get('location')
        file_path = ''
        if image:
            file_path = os.path.join('static', image.filename)
            image.save(file_path)
            
        query = "INSERT INTO listing (title, description, phone_number, email, site_image, location) VALUES (%s, %s, %s, %s, %s)"
        values= (name, description, phone_number, email, file_path, location)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        
    return render_template('detailed_listing.html')

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
        
@app.route('/login', methods=['GET','POST'])
def login():
    logged_in = session.get("logged_in") if session.get("logged_in") else False
    username = session["username"] if session.get("logged_in") else "Guest"
    password = session['password'] if session.get("logged_in") else 'password'
    
    if request.method == 'POST':
        input_username = request.form.get('username')
        input_password = request.form.get('password')

        query = 'SELECT * FROM user WHERE username=%s and password=%s'
        cursor.execute(query, (input_username, input_password))
        user = cursor.fetchone()
        
        if user:
            session["username"] = input_username
            session['password'] = input_password
            session['logged_in'] = True
            print("Authentication successful!")
            return f'Welcome back {input_username}'
        else:
            return redirect(url_for('login'))
        
    return render_template('landing_page.html', username=username, password=password, logged_in=logged_in)
