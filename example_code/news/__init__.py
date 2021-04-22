"""Running website as package.

To run the website after installing requirements: 
1. export FLASK_APP=example_code.news
  - Alternatively, do the following: 
    1) cd example_code (cd stands for change directory, so this navigates you to the appropriate folder)
    2) export FLASK_APP=news
2. python -m flask run
3. Click the link!
"""


import os
from flask import Flask
from flask import render_template


DATE_FORMAT_LENGTH: int = 10
TIME_FORMAT_LENGTH: int = 8
SECRET_KEY_NEWSAPI = "ea435543f4fe4028bbad0ca1ba296041"
# SECRET_KEY_NEWSAPI = os.environ['SECRET_KEY_NEWSAPI']


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # A local database shouldn't be needed, but just in case...
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that serves as the homepage
    @app.route('/') # tells Flask the URL that should trigger a call to our function!
    def home():
        return render_template('home.html')
    
    @app.route('/index')  
    def index():
        """Displays all news articles related to UNC."""
        from newsapi import NewsApiClient
        import json

        # Initialize API KEY
        newsapi = NewsApiClient(api_key=SECRET_KEY_NEWSAPI)
        philippines_articles = newsapi.get_everything(q='unc')
        # asia_articles = newsapi.get_top_headlines(category='asia')
        # all_articles = philippines_articles['articles'] + asia_articles['articles']
        all_articles = philippines_articles['articles']

        article_headline = []
        article_url = []
        article_source = []
        article_author = []
        article_date = []
        article_time = []
        article_description = []
        article_image = []
        article_content = []

        for i in range(len(all_articles)):
            myarticles = all_articles[i]
            article_headline.append(myarticles['title'])
            article_url.append(myarticles['url'])
            article_source.append(myarticles['source']["name"])
            article_author.append(myarticles['author'])
            article_date.append(myarticles['publishedAt'][0:DATE_FORMAT_LENGTH])
            article_time.append(myarticles['publishedAt'][(DATE_FORMAT_LENGTH + 1):(DATE_FORMAT_LENGTH + 1 + TIME_FORMAT_LENGTH)])
            article_description.append(myarticles['description'])
            article_image.append(myarticles['urlToImage'])
            article_content.append(myarticles['content'])
            
        mylist = zip(article_headline, article_url, article_source, article_author, article_date, article_time, article_description, article_image)
        
        return render_template('index.html',mylist=mylist)

    return app