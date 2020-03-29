from flask import Flask, jsonify, request

app= Flask(__name__)

devs=[
    {
        'id': 1,
        'name': 'Michelle',
        'language': 'python'

    },
    {
        'id': 2,
        'name': 'Taylor',
        'language': 'C++'
    },
    {   'id': 3,
        'name': 'Shakira ',
        'language': 'Matlab'

    }
]

@app.route('/',methods=['GET'])
def home():
    return "Hello world :)",200

@app.route('/devs',methods=['GET'])
def dev():
    return jsonify(devs),200

@app.route('/devs/<string:language>',methods=['GET'])
def language(language):
    # devs_language = [i for i in devs if i['language'] == language]
    for i in devs:
        if i['language'] == language:
            devs_language = i
    return jsonify(devs_language),200

@app.route('/devs/<int:id>',methods=['GET'])
def id(id):
    for i in devs:
        if i['id'] == id:
            return jsonify(i), 200
        else:
            return jsonify({'error':'not found'}),404


@app.route('/devs/',methods=['POST'])
def save_data():
    data = request.get_json()
    devs.append(data)
    return jsonify(data),201

@app.route('/devs/<int:id>',methods=['PUT'])
def change(id):
     for i in devs:
         if i['id']==id:
             i['language']= request.get_json().get('language')
             return jsonify(i),200
     return jsonify({'error': 'not found'}),404

@app.route('/devs/<int:id>',methods=['DELETE'])
def remove(id):
     for i in devs:
         if i['id']==id:
             remove_id=i
             devs.remove(remove_id)
             return jsonify({'message': str(id)+' was deleted'}),200



if __name__ == '__main__' :
    app.run(debug=True)





