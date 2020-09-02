from test_scripts import django_setup
from snippets.serializers import SnippetModelSerializer, SnippetSerializer

serializer = SnippetModelSerializer()
print(repr(serializer))

serializer = SnippetSerializer()
print(repr(serializer))

# repr, str 차이? https://shoark7.github.io/programming/python/difference-between-__repr__-vs-__str__
