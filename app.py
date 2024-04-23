from flask import Flask, render_template, url_for, make_response
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/blogs')
def blogs():
    return render_template('blog.html')
@app.route('/blog-12894')
def blog1():
    return render_template('blog1.html')
@app.route('/blog-12994')
def blog2():
    return render_template('blog2.html')

@app.route('/sitemap.xml')
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    pages = []
    ten_days_ago = datetime.datetime.now() - datetime.timedelta(days=10)
    ten_days_ago = ten_days_ago.date().isoformat()

    # static routes
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments) == 0:
            pages.append(
                [url_for(rule.endpoint, _external=True), ten_days_ago]
            )

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"    

    return response

if __name__ == '__main__':
    app.run(debug=True)
