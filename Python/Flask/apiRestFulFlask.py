from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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

class Index(Resource):
    def get(self):
        return people, 200
    
    def post(self):
        data = request.get_json()
        people.append(data)

        return data, 201

class PeoplePerShow(Resource):
    def get(self, favShow):
        for person in people:
            if(person['favShow'] == favShow):
                return person

        return {'error': 'not found'}, 404

class PeoplePerAge(Resource):
    def get(self, age):
        for person in people:
            if(person['age'] == age):
                return person, 200
        
        return {'error': 'not found'}, 404

class UpdatePerson(Resource):
    def put(self, name):
        for person in people:
            if person['name'] == name:
                person['favShow'] = request.get_json().get('favShow')

                return person, 200

        return {'error': 'person not found'}, 404
    def delete(self, name):
        i=0
        for person in people:
            if person['name'] == name:
                del people[i]
                return {'menssage': 'person removed with sucessful'}, 200
            i+=1

api.add_resource(Index, '/people')
api.add_resource(PeoplePerShow, '/people/<string:favShow>')
api.add_resource(PeoplePerAge, '/people/<int:age>')
api.add_resource(UpdatePerson, '/people/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)