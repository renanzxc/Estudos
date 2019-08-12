from flask import Flask, jsonify, request

app = Flask(__name__)

people = [
    {
        "name": "Renan",
        "age": 19,
        "favShow": "Breaking Bad" 
    },
    {
        "name": "João",
        "age": 22,
        "favShow": "Game Of Thrones"
    },
    {
        "name": "Lucas",
        "age": 20,
        "favShow": "MrRobot"
    }
]

#Method GET
@app.route('/people', methods=['GET'])
def index():
    return jsonify(people), 200

@app.route('/people/<string:favShow>', methods=['GET'])
def peoplePerShow(favShow):
    for person in people:
        if(person['favShow'] == favShow):
            return jsonify(person), 200

    return jsonify({'error': 'not found'}), 404

@app.route('/people/<int:age>', methods=['GET'])
def peoplePerAge(age):
    #peopleAge = [person for person in people if people['age'] == age]
    for person in people:
      if(person['age'] == age):
          return jsonify(person), 200

#Method POST
@app.route('/people', methods=['POST'])
def newPerson():
    data = request.get_json()
    people.append(data)

    return jsonify(data), 201

#Method PUT
@app.route('/people/<string:name>', methods=['PUT'])
def updatePerson(name):
    for person in people:
        if person['name'] == name:
            person['favShow'] = request.get_json().get('favShow')

            return jsonify(person), 200

    return jsonify({'error': 'person not found'}), 404

#Method DELETE
@app.route('/people/<string:name>', methods=['DELETE'])
def removePerson(name):
    i=0
    for person in people:
        if person['name'] == name:
            del people[i]
            return jsonify({'mensasge': 'person removed with sucessful'}), 200
        i+=1
    
if __name__ == '__main__':
    app.run(debug=True)