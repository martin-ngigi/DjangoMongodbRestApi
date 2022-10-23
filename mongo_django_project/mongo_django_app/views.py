from django.shortcuts import render

# endpoints are certain urls you can obtain data from

#   YOUTUBE LINK
#https://www.youtube.com/watch?v=i5JykvxUk_A&t=44s

# Create your views here.

from dataclasses import dataclass
from django.http import JsonResponse
from django.urls import is_valid_path
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#POST -> means inserting new record ie Create a new Record
#PUT -> means updating data

#Either fetch or update
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    #fetch data
    if request.method == 'GET':
        # 1. Get all python data
        # 2. Serialize the data(Transform from python to json)
        # 3. Return json data
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)
    
    #Create data
    if request.method == 'POST':
        # 1. Get json data
        # 2. Deserialize It(convert json -> python)
        # 3. Return python data
        serializer = DrinkSerializer(data = request.data)
        #validate
        if serializer.is_valid():
            serializer.save() #save valid data
            return Response(serializer.data, status = status.HTTP_201_CREATED)

# #Either fetch, update delete
@api_view(['GET', 'PUT', 'DELETE'])
def drink_details(request, id, format=None): #id is from urls.py
    try:
        drink=Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Fecth
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    #Update
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        #if serializer is valid, the save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        #else, show error message
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    #Delete
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def drink_details(request, id, format=None): #id is frpm urls.py
#     try:
#         drink = Drink.objects.get(pk=id)
#     except Drink.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DrinkSerializer(drink)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = DrinkSerializer(drink, data=request.data)
#         # if serializer is_valid save data
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         #else show error message
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         drink.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
