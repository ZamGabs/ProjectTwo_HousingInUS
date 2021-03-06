from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import news_scrap

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mortgage_app"
#mongo = PyMongo(app)

# url = "mongodb://test2:test123@ds141613.mlab.com:41613/project_housing_price"
# connection = MongoClient(url)
# db = connection['Housing_project']

connection = pymongo.MongoClient('ds141613.mlab.com', 41613)
db = connection['HousingPricesUS']
db.authenticate('test2', 'test123')


@app.route("/")
def index():
    news_scrap = db.Housing_project.find_one()
    return render_template("index.html", news_scrap=news_scrap)
    # try:
    #     Housing_project = db.Housing_project.find_one()
    #     return render_template("index.html", Housing_project=Housing_project)
    # except:
    #     return redirect("/", code=302)


# @app.route("/price_factors")
# def price_factors():
#     return render_template("price_factors.html")


# @app.route("/timeseries")
# def timeseries():
#     return render_template("timeseries.html")


# @app.route("/leaflet")
# def leaflet():
#     return render_template("leaflet.html")


# @app.route("/data_exploration")
# def data_exploration():
#     return render_template("dataexploration.html")


@app.route("/scrap")
def scraper():

    Housing_project = db.Housing_project
    data = news_scrap.scrap()
    Housing_project.update({}, data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
