from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Servico, Endereco, Perfil
from .serializers import ClienteSerializer, ServicoSerializer, EnderecoSerializer, PerfilSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.db.models import Count, Max, Min, Sum


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    @action(detail=False, methods=['get'])
    def servicos_cliente(self, request):
        cliente_id = request.query_params.get('cliente_id')
        servicos = Servico.objects.filter(cliente_id=cliente_id)
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def servicos_pendentes(self, request):
        cliente_id = request.query_params.get('cliente_id')
        servicos = Servico.objects.filter(cliente_id=cliente_id, status='Pendente')
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def servicos_por_cliente_status(self, request):
        cliente_id = request.query_params.get('cliente_id')
        status = request.query_params.get('status')
        servicos = Servico.objects.filter(cliente_id=cliente_id, status=status)
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)