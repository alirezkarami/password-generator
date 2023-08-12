from .models import Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SendSerializer
import json


# Create your views here.

@api_view(['GET'])
def view(request):
    all = Category.objects.all()
    se_all = SendSerializer(all, many=True)
    return Response(se_all.data)


@api_view(['POST'])
def send(request):
    name = request.data.get('name')
    pass_id = json.loads(request.data.get('pass_id'))
    passes = Category(name=name)
    passes.save()
    passes.pass_id.set(pass_id)
    passes.save()
    se_pass = SendSerializer(passes)
    return Response(se_pass.data)
