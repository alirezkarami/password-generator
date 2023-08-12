from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Group
from .serializers import SendSerializer
import json


# Create your views here.


@api_view(['GET'])
def view(request):
    all = Group.objects.all()
    se_all = SendSerializer(all, many=True)
    return Response(se_all.data)


@api_view(['POST'])
def send(request):
    name = request.data.get('name')
    users = json.loads(request.data.get('users'))
    groups = Group(name=name)
    users.save()
    groups.users.set(users)
    users.save()
    se_users = SendSerializer(groups)
    return Response(se_users.data)
