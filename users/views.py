from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Utilisateur
from .serializers import UtilisateurSerializer


@api_view(['GET'])
def get_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    utilisateurs_with_notes = []
    for utilisateur in utilisateurs:
        if utilisateur.note is not None:
            utilisateurs_with_notes.append(utilisateur)
    serializer = UtilisateurSerializer(utilisateurs_with_notes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_utilisateur(request):
    serializer = UtilisateurSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_utilisateur(request, pk):
    try:
        utilisateur = Utilisateur.objects.get(pk=pk)
    except Utilisateur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UtilisateurSerializer(utilisateur)
    return Response(serializer.data)


@api_view(['PUT'])
def update_utilisateur(request, pk):
    try:
        utilisateur = Utilisateur.objects.get(pk=pk)
    except Utilisateur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UtilisateurSerializer(utilisateur, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_utilisateur(request, pk):
    try:
        utilisateur = Utilisateur.objects.get(pk=pk)
    except Utilisateur.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    utilisateur.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
