#########################################
##### Name:                         #####
##### Uniqname:                     #####
#########################################

## Setup
from flask import Flask, render_template, request, redirect
import json
import requests
import secrets
app = Flask(__name__)

## Name page
@app.route('/name/<visitor_name>')
def visit_name(visitor_name):
    return render_template('name.html', visitor_name=visitor_name.capitalize())

## Headlines page
@app.route('/headlines/<visitor_name>')
def visit_headlines(visitor_name):
    headlines_list = get_headlines()
    return render_template('headlines.html', visitor_name=visitor_name.capitalize(), headlines_list=headlines_list)

## Images page
@app.route('/images/<visitor_name>')
def visit_images(visitor_name):
    headlines_list = get_headlines()
    return render_template('images.html', visitor_name=visitor_name.capitalize(), headlines_list=headlines_list)

## 404 redirect
@app.errorhandler(404)
def not_found(e):
    return redirect("/name/doe")

## Get headlines
def get_headlines():
    '''Make a request to the NYT API and return the top 5 technology headlines
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        list of 5 dicts, each containing the title, url, and thumbnail image url of an NYT article
    '''
    baseurl = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    params = {"api-key": secrets.API_KEY}
    response = requests.get(baseurl, params=params).json()
    
    headlines_list = []
    for i in range(5):
        headline = {}
        headline['title'] = response['results'][i]['title']
        headline['url'] = response['results'][i]['url']
        headline['thumb'] = response['results'][i]['multimedia'][0]['url']
        headlines_list.append(headline)
    
    return headlines_list

## Run flask
if __name__ == '__main__':
    app.run()