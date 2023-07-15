
""" create the link"""
 
from flask import Flask
from flask_restful import Resource, Api,reqparse,abort

app = Flask(__name__)
api = Api(app)


# class helloworld(Resource):
#     def get(self):
#         return {"data":'hello ragul'}
    
Todo = {
   1: {"name":"ragul you are great",
    "summary":"ragul rathna @ securekloud intern "}
}


arg_post = reqparse.RequestParser()
arg_post.add_argument("task",type= str,help="task must",required=True)
arg_post.add_argument("summary",type= str,help = "summary must",required = True )



class doo(Resource):
    def get(self):
        return Todo
    

class todo(Resource):
    def get(self,todo_id):
        return Todo[todo_id]
    
    def post(self,todo_id):
        arg = arg_post.parse_args()
        if todo_id in Todo:
            abort(409,"alredy")
        Todo[todo_id] = {"task" : arg["task"] , "summary" : arg["summary"]}
        return Todo[todo_id]


class Helloworld(Resource):
    def get(self,name):
        return {'hello':'{}'.format(name)}
    


api.add_resource(doo,'/doo')
# api.add_resource(helloworld,'/helloWorld')
api.add_resource(Helloworld,'/Helloworld/<string:name>')
api.add_resource(todo,'/todo/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
