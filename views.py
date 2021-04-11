from django.shortcuts import render
from rest_framework.views import APIView #for creating API
from rest_framework.response import Response #to return Response

from .models import *
# Creating views here.
class TodoView(APIView):

    #GET : 
    def get(self , request):
        response ={}
        response['status'] = 500
        response['message'] = "Something went wrong"
        try:
            todo_objects = Todo.objects.all()
            # print(todo_objects)
            payload = []
            for each_objects in todo_objects:
                payload.append({
                    'todo_id' : each_objects.id,
                    'todo_name' : each_objects.todo_name,
                    'todo_description' : each_objects.todo_description,
                    'is_completed' : each_objects.is_completed
                })
            
            response['status'] = 200
            response['message'] = 'All todos'
            response['data'] = payload
        except Exception as e:
            print(e)
        
        return Response(response)
    #POST : 
    def post(self,request):
        response = {}
        response['status'] : 500
        response['message'] : "Something went wrong"

        try:
            data = request.data
            print(data)
            todo_name = data.get('todo_name')
            todo_description = data.get('todo_description')

            if todo_name is None:
                response['message'] = "Todo_name is required"
                raise  Exception('Todo name is not found')
            if todo_description is None:
                response['message'] = "Todo_description is required"
                raise  Exception('Todo description is not found')
            
            create_data = Todo.objects.create(
                todo_name = todo_name,
                todo_description = todo_description
            ) 
            payload = {'todo_id' :create_data.id , 'todo_name' : create_data.todo_name , 'todo_description' : create_data.todo_description}
            response['status'] = 200
            response['message'] = "Your todo is saved"
            response['data'] = payload
            return Response(response)
        except Exception as e:
            print(e)

        return Response(response)
        
    #DELETE:
    def delete(self,request):
        response = {}
        response['status'] : 500
        response['message'] : "Something went wrong"
        
        

        try:
            todo_id = request.GET.get('todo_id')
            if todo_id is None:
                response['message'] = 'Todo_id is required'
                raise Exception("Todo_id is not found")
            try:
                todo_object = Todo.objects.get(id = todo_id)
                todo_object.delete()
                response['message'] = "Data deleted successfully"
            except Exception as e:
                response['message'] = 'invalid todo id'

        except Exception as e:
            print(e)
        
        return Response(response)

    def put(self,request):
        response = {}
        response['status'] : 500
        response['message'] : "Something went wrong"
        try:
            updated_data = request.data
            print(updated_data)
            todo_id = updated_data.get('todo_id')
            updated_todo_name = updated_data.get('todo_name')
            updated_todo_description = updated_data.get('todo_description')
            updated_is_completed = updated_data.get('is_completed')

            try:
                todo_object = Todo.objects.get(id = todo_id)
                todo_object.todo_name = updated_todo_name
                todo_object.todo_description = updated_todo_description
                todo_object.is_completed = updated_is_completed
                todo_object.save()

                response['message'] = "Data updated successfully"
                return Response(response)
            except Exception as e:
                response['message'] = "Invalied todo id"
                return Response(response)
            
                
        except Exception as e:
            print(e)
        


def index(request):
    return render(request , 'index.html')