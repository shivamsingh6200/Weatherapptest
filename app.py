import requests
from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/weather",methods=['POST','GET'])
def searchpage():
    apikey="602e11c0c9bf90c661e13498979c2a9d"
    url="https://api.openweathermap.org/data/2.5/weather"

    para={"q":request.form.get("city"),
     "units":"imperial",
     "appid":apikey
     }
    
    response=requests.get(url,params=para)
    data=response.json() 
    weather = {
            'city' :para["q"].upper(),
            'temperature' :"%.1f" % float((data['main']['temp']-32)/1.8),
            'description' : data['weather'][0]['description'],
            'icon' : data['weather'][0]['icon'],
        }
    print (weather)
    return render_template("weather.html",weather=weather)

if __name__=="__main__":
    app.run(host="0.0.0.0" , port = 5002)