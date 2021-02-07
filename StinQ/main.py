from flask import Flask
from flask import jsonify
from flask import request
from QueueOps import *
import json

app = Flask(__name__)
queueOps = StinQueue()

@app.route('/')
def healthCheck():
   return jsonify({
       'success':True
   })

@app.route('/pushtoqueue/<queuename>')
def pushToQueue(queuename):
    dataFromRequest = request.data.decode()
    message = json.dumps(dataFromRequest)
    queuePushResponse = queueOps.pushToQueue(queuename, message)
    return jsonify({
        'success': queuePushResponse.isSuccess,
        'positionInQueue': queuePushResponse.data,
        'error': queuePushResponse.errorList
    });

@app.route('/getfromqueue/<queuename>')
def getFromQueue(queuename):
    message = queueOps.getFromQueue(queuename)
    if (message != None):
        return jsonify({
            'isMessage': True,
            'message':message
        })
    return jsonify({
        'isMessage': False
    })
    
if __name__ == '__main__':
   app.run()