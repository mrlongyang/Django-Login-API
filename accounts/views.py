from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"message": "Login successful", "username": user.username})
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)

############## 
✅ Step 8: Test in Postman
Method: POST

URL: http://127.0.0.1:8000/api/login/

Body: (raw JSON)

json
Copy
Edit
{
  "username": "your_username",
  "password": "your_password"
}
Expected Response (200 OK):

json
Copy
Edit
{
  "message": "Login successful",
  "username": "your_username"
}
If Failed (401 Unauthorized):

json
Copy
Edit
{
  "message": "Invalid credentials"
}

✅ Step 3: Test in Postman
Method: POST

URL: http://127.0.0.1:8000/api/register/

Body (raw JSON):

json
Copy
Edit
{
  "username": "newuser",
  "password": "newpassword"
}
Expected Responses:

201 Created:

json
Copy
Edit
{
  "message": "Registration successful"
}
400 Bad Request (if username exists):

json
Copy
Edit
{
  "message": "Username already exists"
