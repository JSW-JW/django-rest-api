from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins

from django.shortcuts import get_object_or_404

from .serializers import StatusSerializer
from ..models import Status

import json


# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         pass

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class StatusAPIView(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    passed_id = None

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    # def get_object(self):
    #     id = json.loads(self.request.body).get('id')
    #     queryset = self.get_queryset()
    #
    #     obj = get_object_or_404(queryset, id=id)
    #     return obj

    def get(self, request, *args, **kwargs): # overrides 'get' method from ListAPIView
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        print(request.body)
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        print(request.body)
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)
        requested_id = request.data.get('id')

        passed_id = url_passed_id or new_passed_id or requested_id or None
        self.passed_id = passed_id

        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        print(request.body)
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id

        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        print(request.body)
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id

        return self.destroy(request, *args, **kwargs)


# class StatusDetailAPIView(mixins.DestroyModelMixin,
#                           mixins.UpdateModelMixin,
#                           generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class StatusDetailAPIView(generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
#
#
#     def get(self, *args, **kwargs):
#         kwargs = self.kwargs
#         kw_id = kwargs.get('id')
#         try:
#             obj = Status.objects.get(id=kw_id)
#             return obj
#         except Status.DoesNotExist:
#             return Response({"detail":"model not found"}, status=404)

