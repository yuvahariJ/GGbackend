import os
import json
from flask import request
from flask import Flask
import pickle
import json

auto_fertlize=False
auto_watering=False
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'
@app.route('/temperature')
def temp():
    #def get_temperature_average():
    op1=open(r'C:\Users\User\Desktop\flask\ref\temperature.pickle','rb')
    l=pickle.load(op1)
    op1.close()
    avg=(round((sum(l['values'])/7),2))

#def get_temperature_weekly_readings():
    op1=open(r'C:\Users\User\Desktop\flask\ref\temperature.pickle','rb')
    l=pickle.load(op1)
    op1.close()
    dic={}
    dic["dates"]=[]
    dic["values"]=[]
    for i in range(len(l['dates'])):
        dic["dates"].append(l['dates'][i])
        dic["values"].append(l['values'][i])
    dic["averge"]=avg
    #dic["averge"].append(avg)
    return (json.dumps(dic))

    s=get_tempearture()
    return(s)
@app.route("/onoff",methods=["GET"])
def on():
    waon=request.args['waon']
    if(waon==1):
        return 1
    else:
        return 0
@app.route('/humidity')
def humi():
    #def get_temperature_average():
    op1=open(r'C:\Users\User\Desktop\flask\ref\humidity.pickle','rb')
    l=pickle.load(op1)
    op1.close()
    avg=(round((sum(l['values'])/7),2))

#def get_temperature_weekly_readings():
    op1=open(r'C:\Users\User\Desktop\flask\ref\humidity.pickle','rb')
    l=pickle.load(op1)
    op1.close()
    dic={}
    dic["dates"]=[]
    dic["values"]=[]
    for i in range(len(l['dates'])):
        dic["dates"].append(l['dates'][i])
        dic["values"].append(l['values'][i])
    dic["averge"]=avg
    #dic["averge"].append(avg)
    return (json.dumps(dic))

    s=get_humidity()
    return(s)


@app.route('/fertiliserdate')
def fertidate():
    return 23

@app.route('/wateringdate')
def waterdate():
    return 23

@app.route('/wateringtime')
def watertime():
    return 23

@app.route('/home')
def home():
    #def getLastFertilized():
    open2=open(r'C:\Users\User\Desktop\flask\ref\fertilize.pickle','rb')
    l=pickle.load(open2)
    open2.close()
    last_fert=(l[-1])
#def getLast_Watered_date():
    open2=open(r'C:\Users\User\Desktop\flask\ref\watering.pickle','rb')
    l=pickle.load(open2)
    open2.close()
    last_water_date=(l['dates'][-1])
#def getLast_Watered_time():
    open2=open(r'C:\Users\User\Desktop\flask\ref\watering.pickle','rb')
    l=pickle.load(open2)
    open2.close()
    k=l['time'][-1]
    s=""
    for i in k:
        s=s+str(i)+":"
    last_water_time=(s[:-1])
#def water_Fertilize:
    open1=open(r"C:\Users\User\Desktop\flask\ref\watering.pickle",'rb')
    j=pickle.load(open1)
    open1.close()
    water_rep=j["dates"]
    open1=open(r"C:\Users\User\Desktop\flask\ref\fertilize.pickle",'rb')
    j=pickle.load(open1)
    open1.close()
    fertilize_rep=j
#def auto_ferilize:
    dic1={}
    dic1["lastFertilzed"]=last_fert
    dic1["lastWaterDate"]= last_water_date
    dic1["lastWaterTime"]=last_water_time
    dic1["autoFertlize"]=auto_fertlize
    dic1["autoWatering"]=auto_watering
    dic1["waterReport"]=water_rep
    dic1["fertilizeReport"]=fertilize_rep

    return(json.dumps(dic1))
    s=get_home()
    return(s)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
