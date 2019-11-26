from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from content.api.serializers import productSerializer
from content.models import product


class all(APIView):
    @api_view(['GET', ])
    def api_homePage(request, pk):
        prod = product.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = productSerializer(prod)
            return Response(serializer.data)

class listView(ListAPIView):
    queryset = product.objects.all()
    serializer_class = productSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'category__gender')

