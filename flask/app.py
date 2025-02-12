from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

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
        name = request.form.get('site_Name')
        description = request.form.get('description')
        phone_number = request.form.get('number')
        email = request.form.get('email')
        image = request.files.get('picture')
        listings = []

        if image:
            file_path = os.path.join('uploads', image.filename)
            image.save(file_path)

            listing = {
                'name': name,
                'description': description,
                'phone Number': phone_number,
                'email': email,
                'image': file_path
            }

            listings.append(listing)

            with open('listings.json', 'w') as f:
                json.dump(listings, f)

            return f'Site uploaded with success!'
    
    return render_template('detailed_listing.html')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
 
