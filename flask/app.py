from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def citing():
    sites=[
        {
            'h3':'Cameroon Wildlife Sanctuary',
            'src' : 'https://th.bing.com/th?id=OLC.O68LFm1CMNRzOg480x360&w=186&h=140&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2',
            'p' : 'A beautiful sanctuary that offers a close encounter with Cameroon\'s diverse wildlife.'
        },
          {
            'h3':'Kribi Beach Resort',
            'src' : 'https://bing.com/th?asid=432345564512219874&id=OAUMA.F2F177B5E000C96EBAEE9C5E37509F32_6E224B1B23B99A05&pid=21.1&o=5&w=296&h=222&rs=2&qlt=100',
            'p' : 'Experience the clean, sandy beaches of Kribi, perfect for a relaxing vacation.'
        },
            {
            'h3':'Mount Cameroon',
            'src' : 'https://th.bing.com/th?id=OLC.HV3WQRT52692tw480x360&w=186&h=140&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2',
            'p' : 'Take an adventurous hike up the tallest mountain in West Africa.'
        }
    ]
    
    return render_template('publicListing.html', listing=sites)