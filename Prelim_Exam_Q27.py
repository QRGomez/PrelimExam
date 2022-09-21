from crypt import methods
from flask import Flask, jsonify,request

app = Flask(__name__)
heart_info = [
        {
            "heart_id": "0001",
            "heart_date": "Sept 21, 2022",
            "heart_rate": "74bpm"
        },
        {
            "heart_id": "0002",
            "heart_date": "Sept 17, 2022",
            "heart_rate": "80bpm"
        },
]

@app.route('/heart', methods=['GET'])
def getHeart():
    return jsonify(heart_info)
@app.route('/heart', methods=['POST'])
def updateHeart():
    heart_Stored = request.get_json()
    heart_info.append(heart_Stored)
    return {'id' : len(heart_info)},200
@app.route('/heart', methods=['DELETE'])
def Delete_Heart():
    heart_info.pop(heart_info)
    return None,200

if __name__ == '__main__':
    app.run()