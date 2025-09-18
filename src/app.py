from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'message': 'Hello World',
        'time': datetime.datetime.now().strftime("%I:%M%:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message' : 'You are doing a great job, my friend!!!!'
        })

@app.route('/api/v1/healthz')

def health():
    return jsonify({
        'status': 'It is UP',
        'time': datetime.datetime.now().strftime("%I:%M%:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message' : 'You are doing an AWESOME job, my friend!!'
        })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

# '/api/v1/details'
# '/api/v1/healthz'

# from flask import Flask, jsonify
# import socket

# app = Flask(__name__)

# @app.route('/api/v1/details')
# def details():
#     return jsonify({
#         'hostname': socket.gethostname()
#     })
    
# if __name__=='__main__':
#     app.run(debug=True)