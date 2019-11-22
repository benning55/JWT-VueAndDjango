# from rest_framework import status
# from django.contrib.auth.models import User
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from movies.api.serializers import UserSerializer
#
#
# # Create your views here.
#
#
# @api_view(['POST'])
# def create_user(request):
#     serialized = UserSerializer(data=request.DATA)
#     if serialized.is_valid():
#         User.objects.create_user(
#             serialized.init_data['email'],
#             serialized.init_data['username'],
#             serialized.init_data['password'],
#         )
#         return Response(serialized.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # """
# #     User View!
# # """
# #
# #
# # class UserList(generics.ListAPIView):
# #     queryset = User.objects.all().order_by('first_name')
# #     serializer_class = UserSerializer
# #     permission_classes = (permissions.IsAuthenticated,)
# #
# #
# # class UserCreate(generics.CreateAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer
# #     permission_classes = (permissions.IsAdminUser, )
# #
# #
# # class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer
# #     permission_classes = (permissions.IsAuthenticated, )
# #
# #
# # """
# #     Genre View!
# # """
# #
# #
# # class GenreListCreate(generics.ListCreateAPIView):
# #     """ List and create genres """
# #     queryset = Genre.objects.all()
# #     serializer_class = GenreSerializer
# #     permission_classes = (permissions.IsAuthenticated, )
# #
# #
# # class GenreRetrieveUpdate(generics.RetrieveUpdateAPIView):
# #     """ Retrieve and update Genre information """
# #     queryset = Genre.objects.all()
# #     serializer_class = GenreSerializer
# #     permission_classes = (permissions.IsAuthenticated, )
# #
# #
# # """
# #  Movie View!
# # """
# #
# #
# # class MovieListCreate(generics.ListCreateAPIView):
# #     """List and create movies """
# #     queryset = Movie.objects.all().order_by('name')
# #     serializer_class = MovieSerializer
# #     permission_classes = (permissions.IsAuthenticated, )
# #
# #
# # class MovieRetrieveUpdate(generics.RetrieveUpdateAPIView):
# #     """Retrieve and update a movie"""
# #     queryset = Movie.objects.all()
# #     serializer_class = MovieSerializer
# #     permission_classes = (permissions.IsAuthenticated, )
# #
# #
# # """
# #     Comment View!
# # """
# #
# #
# # class CommentListCreate(generics.ListCreateAPIView):
# #     """ List or create a movie """
# #     queryset = Comment.objects.all()
# #     serializer_class = CommentSerializer
# #     permission_classes = (permissions.IsAuthenticated, )
# #
# #
# # class CommentRetrieveUpdate(generics.RetrieveUpdateAPIView):
# #     """ List or create a movie """
# #     queryset = Comment.objects.all()
# #     serializer_class = CommentSerializer
# #     permission_classes = (permissions.IsAuthenticated, )
#
#
