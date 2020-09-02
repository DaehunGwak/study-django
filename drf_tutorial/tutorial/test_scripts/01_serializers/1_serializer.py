from test_scripts import django_setup
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)
print(type(serializer.data), serializer.data)

content = JSONRenderer().render(serializer.data)
print(type(content), content)

stream = io.BytesIO(content)
data = JSONParser().parse(stream)
print(type(data), data)

serializer = SnippetSerializer(data=data)
print(serializer.is_valid())
print(serializer.validated_data)
print(serializer.save())

queryset = Snippet.objects.all()
serializer = SnippetSerializer(queryset, many=True)
print(len(serializer.data), serializer.data)
