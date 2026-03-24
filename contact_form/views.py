from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactQuery
from .serializers import ContactQuerySerializer

class ContactSubmitView(APIView):
    def post(self, request):
        serializer = ContactQuerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contact query submitted successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
