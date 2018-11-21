from flask import Flask,render_template,jsonify
from volumeScripts.vol_SN import modelrunSN
from volumeScripts.vol_CH import modelrunCH
from volumeScripts.vol_EU import modelrunEU
from volumeScripts.vol_USA import modelrunUS
from volumeScripts.vol_IN import modelrunIN
import json
from trendanalyis.getdata import get_data
from ML_DELL.dell_data.series_job.series_job import series_job
from ML_DELL.dell_data.series_location.init import series_location
from ML_DELL.dell_data.location_marketing.location_marketing import location_marketing
from ML_DELL.laptop_prices.laptop_price import laptop_price

from productconfig.getdatapc import get_data_pc

app=Flask(__name__)
# app.config["REDIS_URL"] = "redis://localhost:5000"
# app.register_blueprint(sse, url_prefix='/stream')

@app.route('/charts/<relationship>')
def charts(relationship):
    data = None

    if relationship == "warranty":
        max=2
        r="Warranty Purchase"
    elif relationship == "sj":
        r="Product Series"
        max=5
        data=series_job()
    elif relationship == "lm":
        r="Marketing Target"
        max=5
        data=location_marketing()
    rel={
        'relationship':r,
        'max':max
    }
    
    
    # print(data['Arr1'])
    return render_template('charts.html',data1=data['test'],data2=data['predictions'],rel = rel['relationship'],max=rel['max'])



@app.route('/prodconfig')
def pc():
    data = laptop_price()
    test=data['test']
    pred = data['predictions']

    return render_template('prodconfig.html',test=test,pred=pred)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/volume/<country>')
def volume(country):

    data=None
    if country == "India":
         data=modelrunIN()
    elif country == "China":
        data=modelrunCH()
    elif country == "USA":
        data=modelrunUS()
    elif country == "Europe":
        data=modelrunSN()
    elif country == "Singapore":
        data = modelrunSN()
    print(data) 
    return render_template('volumes.html',country=country,datatest=data['test'],datapred=data['predictions'])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/forecast')
def forecast():
    return render_template('forecast.html')

if __name__ == "__main__":
    app.run(debug=True)