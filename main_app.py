import os
from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from processing import scraper

app = Flask(__name__)
app.config["DEBUG"] = True

#CSFR Protection routine
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)
csrf.init_app(app)

#render main page
@app.route('/', methods = ["GET", "POST"])
def input_page():
    errors = ""
    if request.method == "POST":
        url = None
        url = request.form['url']
      
        if url is not None:
            
            try:
                h1 = scraper(url)[0]
                h2 = scraper(url)[1]
                h3 = scraper(url)[2]
                p = scraper(url)[3]
                return render_template("results.html", h1=h1, h2=h2, h3=h3, p=p)
            
            except Exception as e:
                #errors = "🐸 The anti-bug frog has caught something! Can you try again with another site? Sorry, it's still a beta version!"
                 errors = e   

    return render_template("main.html", errors=errors)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
