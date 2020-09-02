from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetModelSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetModelSerializer(snippets, many=True)
        """
        Tip Memo. 
        JsonResponse에 dict가 들어오지 않으면 raise TypeError 가 됨
        따라서 `safe=False` 를 하여 다른 타입의 객체가 들어올 수 있도록 허용해줘야 함
        https://docs.djangoproject.com/en/3.1/ref/request-response/#jsonresponse-objects 
        """
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)  # Not found

    if request.method == 'GET':
        serializer = SnippetModelSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetModelSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)  # Bad request

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)  # No content
