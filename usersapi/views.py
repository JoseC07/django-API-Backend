from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)



class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class workoutapi(APIView):
    @method_decorator(login_required, name='login') 
    
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', -1)
        print(id)

        if id <= -1:
            workouts = workout.objects.all()
            serializer = workoutSerializer(workouts, many =True)
            print('if')
        else:
            try:
                workouts = workout.objects.get(id=id)
            except workout.DoesNotExist:
                # We have no object! Do something...
                pass
            
            serializer = workoutSerializer(workouts, many =False)
            print('else')
        
        
        return Response(serializer.data)

    def post(self,request,format= None):
        data = request.data
        print(data)

            
        #  if serializer.is_valid():
        #      serializer.save()
        #      return Response(serializer.data, status=status.HTTP_201_CREATED)
        return # Response(serializer.errros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id', -1)
       
        wi = workout.objects.get(id=id)
        wi.delete()
        res = {'msg':'workout Deleted Successfully!'}
        return Response(res)
    
    def patch(self, request,*args, **kwargs):
        id = kwargs.get('id', -1)
        workout = workout.objects.get(id=id)
        serializer = workoutSerializer(data=request.data,instance=workout,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'workout Updated Successfully!'})
        return Response(serializer.errros, status=status.HTTP_400_BAD_REQUEST)