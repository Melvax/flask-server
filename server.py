# from flask_cors import CORS
from flask import Flask, request,jsonify
import os

app = Flask(__name__)

#My api route 

@app.route("/api/rooms")
def api():
    rooms = {"rooms":["abc","xyz","squaresense"]}
    print(rooms)
    return rooms

@app.route("/occupancy")
def occupancy():
    occupancy=0
    args = request.args
    print('sensor')
    sensor = args.get("sensor")
    print(sensor)
    try:
        file_list = os.listdir("./data/"+sensor)
        sortedlist = sorted(file_list,reverse=True)   
        print(sortedlist)
        last_entry = sortedlist[0]
        in_value = last_entry[-2]
        out_value = last_entry[-1]

        occupancy =  int(in_value)-int(out_value)
    except:
        occupancy="no room data"
    return {"inside":occupancy}

@app.route("/api/webhook",methods=["POST","GET"])
def mywebhook():

    if request.method == 'POST':
        print('start post webhook')
        print("sensor : ",request.get_json().get('sensor'))
        print("ts : ",request.get_json().get('ts'))
        print("in : ",request.get_json().get('in'))
        print("out : "  ,request.get_json().get('out'))
        print('end post webhook')

        ts= request.get_json().get('ts')
        in_value = request.get_json().get('in')
        out_value = request.get_json().get('out')

        file_name = ts+str(in_value)+str(out_value)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dest_dir = os.path.join(script_dir, './data/', 'abc')
        try:
            os.makedirs(dest_dir)
        except OSError:
            pass # already exists
        path = os.path.join(dest_dir, file_name)
        output = open(os.path.join(dest_dir, file_name), 'wb')
      
            
            # stream.write('foo\n')
        return {'request':'200 OK'}
    else :
        return {'request':'GET'}
        
        
    



@app.route("/abc",methods=["POST","GET"])
def abc():
    # if request.method=="GET":
    print("hola")
    # return{"abc":}

if __name__=="__main__":
    app.run(debug=True)


