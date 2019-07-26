from flask import Flask,request,redirect,render_template
from flask_restful import Resource, Api
import json
import requests

app = Flask(__name__)
@app.route('/', methods=['POST'])

def req():
    if request.method=='POST':
        jsondata = request.get_json()
        parameters=jsondata['queryResult']['parameters']

        url = parameters['url']
        title = parameters['title']
        defect_type = parameters['defect_type']
        system_information = parameters['system_information']
        priority = parameters['priority']
        detector = parameters['detector']
        error_message = jsondata['queryResult']['queryText']
        issue = { 
            #'url' : url,
            'title' : title,
            #'defect_type' : defect_type,
            #'system_information' : system_information,
            #'priority' : priority,
            'asignee' : detector,
            'body' : error_message,
            #'labels' : 'bug'
        }
        issue = json.dumps(issue)
    
        headers = {'Content-Type' : 'application/x-www-form-urlencoded',
                'User-Agent': 'junan146',
                'Authorization': 'token adb63d48b18310967a1ad76d869111293a10fd90'
        }
        r = requests.post(
        'https://api.github.com/repos/junan146/buggy/issues', headers=headers, data=issue
)
        return "posted"
    else:
        return 'error'
@app.route('/')
def hello_world():
    return 'hello world!'
        
   

if __name__ == '__main__':
    app.run()
