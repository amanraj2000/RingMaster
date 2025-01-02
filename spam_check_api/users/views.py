from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import User, Contact, Spam
from .serializers import UserSerializer, ContactSerializer, SpamSerializer


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        name = request.data.get('name')
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        email = request.data.get('email', None)

        if User.objects.filter(phone_number=phone_number).exists():
            return Response({"error": "Phone number already registered"}, status=status.HTTP_400_BAD_REQUEST)
        
        hashed_password = make_password(password)

        user = User.objects.create(name=name, phone_number=phone_number, password=hashed_password, email=email)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(phone_number=phone_number)
    except User.DoesNotExist:
        return Response({"error": "User Does Not Exists"}, status=status.HTTP_401_UNAUTHORIZED)
    
    if check_password(password, user.password):
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
    
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def mark_spam(request):
    phone_number = request.data.get('phone_number')
    user = request.user
    if Spam.objects.filter(phone_number=phone_number).exists():
        return Response({"message": "This number is already marked as spam"}, status=status.HTTP_200_OK)
    Spam.objects.create(phone_number=phone_number, reported_by=user)
    return Response({"message": "Number marked as spam"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def search_by_name(request, name):
    users = User.objects.filter(name__icontains=name).order_by('name')
    
    if not users: 
        return Response({'message': 'No users found matching the name.'}, status=404) 

    results = UserSerializer(users, many=True).data
    return Response(results)


@api_view(['GET'])
def search_by_phone_number(request, phone_number):
    users = User.objects.filter(phone_number=phone_number)
    if users.exists():
        results = UserSerializer(users, many=True).data
    else:
        contacts = Contact.objects.filter(phone_number=phone_number)
        results = ContactSerializer(contacts, many=True).data
    return Response(results)
