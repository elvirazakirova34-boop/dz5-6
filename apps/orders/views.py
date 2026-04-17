from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        order = self.get_object()
        order.status = 'accepted'
        order.save()
        return Response({'status': 'Order accepted'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        order = self.get_object()
        order.status = 'closed'
        order.save()
        return Response({'status': 'Order closed'}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

