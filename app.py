from flask import Flask,render_template
from volumeScripts.vol_SN import modelrunSN
from volumeScripts.vol_CH import modelrunCH
from volumeScripts.vol_EU import modelrunEU
from volumeScripts.vol_USA import modelrunUS
from volumeScripts.vol_IN import modelrunIN

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('charts.html ')

@app.route('/volume/<country>')
def volume(country):

    data=None
    if country == "IN":
         data=modelrunIN()
    elif country == "CH":
        data=modelrunCH()
    elif country == "US":
        data=modelrunUS()
    elif country == "EU":
        data=modelrunSN()
    elif country == "SN":
        data = modelrunSN()

    
    return render_template('volume.html',country=country,data=data)


if __name__ == "__main__":
    app.run(debug=True)