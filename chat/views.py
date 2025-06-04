from openai import OpenAI
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .serializers import RegisterSerializer
from .models import ChatMessage
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

client = OpenAI(api_key=settings.OPEN_API_KEY)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"message": "User created"}, status=status.HTTP_201_CREATED)


class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="ChatBot Messaging",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['message'],
            properties={
                'message': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        responses={200: openapi.Response('Bot reply')}
    )
    def post(self, request):
        user_input = request.data.get("message", "")
        reply = self.message_communication_with_bot(user_input)

        ChatMessage.objects.create(
            author=request.user,
            message=user_input,
            reply=reply
        )

        return Response({"reply": reply})

    def message_communication_with_bot(self, msg):
        try:
            response = client.chat.completions.create(

                model="gpt-4o-mini",
                store=True,
                messages=[
                    {"role": "user", "content": msg}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return "OpenAI Error: You may have exceeded your usage quota."


class ChatHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        history = ChatMessage.objects.filter(author=request.user).order_by('-timestamp').values(
            "message", "reply", "timestamp")

        return Response({"history": history}, status=status.HTTP_200_OK)
