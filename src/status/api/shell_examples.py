from six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from .serializers import StatusSerializer
from ..models import Status


'''
Serialize a single object
'''
obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)


'''
Serialize a queryset
'''
qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)


'''
CREATE obj
'''
data = {'user': 1}
serializer = StatusSerializer(data=data)
if serializer.is_valid():
    serializer.save()


'''
UPDATE obj
'''
obj = Status.objects.first()
data = {
    'user': 1,
    'content': 'some new content'
}
update_serializer = StatusSerializer(obj, data=data)
if update_serializer.is_valid():
    updated_status = update_serializer.save()


'''
DELETE obj
'''
data = {'user': 1, 'content': 'please delete me'}
create_serializer = StatusSerializer(data=data)
if create_serializer.is_valid():
    create_obj = create_serializer.save()
    print(create_obj)


serializer = StatusSerializer(obj)
if update_serializer.is_valid():
    updated_status = update_serializer.save()


from rest_framework import serializers
class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()


data = {'content': 'content for customSerializer'}
custom_serializer = CustomSerializer(data=data)
if custom_serializer.is_valid():
    print(custom_serializer.data)