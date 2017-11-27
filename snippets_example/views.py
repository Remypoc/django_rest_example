from snippets_example.models import Snippet
from snippets_example.serializers import SnippetSerializer
from rest_framework import viewsets


# ModelViewSet provide default crud operations
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save()
