from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)



from rest_framework import status
from medical_store.forms import ProductForm
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_medicine(request):
    form = ProductForm(request.data)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)





from medical_store.models import medicine
from .serializers import ProductSerializer
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def retrieve_medicine(request):
    products = medicine.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)




from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_medicine(request, pk):
    product = get_object_or_404(medicine, pk=pk)
    form = ProductForm(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_medicine(request, pk):
    try:
        product = medicine.objects.get(pk=pk)
    except medicine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")


@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def search_medicine(request):
    search_term = request.GET.get('search','')
    med= medicine.objects.filter(name__icontains=search_term)
    serializer=ProductSerializer(med,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def logout(request):
    request.auth.delete()
    return Response("logout successfull", status=status.HTTP_200_OK)