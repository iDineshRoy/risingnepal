from django.urls import path
from django.http import JsonResponse

from django.urls import path


class BaseRouter:
    model = None
    base_name = None
    registry = []

    @classmethod
    def register_viewset(cls, viewset):
        cls.registry.append(viewset)

    @classmethod
    def get_urls(cls):
        urls = []
        for viewset in cls.registry:
            urls.extend(cls.get_urls_for_viewset(viewset))
        return urls

    @classmethod
    def get_urls_for_viewset(cls, viewset):
        base_name = viewset.base_name or viewset.get_name()
        model_name = viewset.model.__name__.lower()

        urlpatterns = [
            url(
                r"^{}/$".format(model_name),
                viewset.as_view(
                    {
                        "get": "list",
                        "post": "create",
                    }
                ),
                name="{}_list".format(base_name),
            ),
            url(
                r"^{}/(?P<pk>\d+)/$".format(model_name),
                viewset.as_view(
                    {
                        "get": "retrieve",
                        "put": "update",
                        "patch": "partial_update",
                        "delete": "destroy",
                    }
                ),
                name="{}_detail".format(base_name),
            ),
        ]

        return urlpatterns

    def __init__(self):
        self.base_name = self.base_name or self.model.__name__.lower()

    # def get_urls(self):
    #     urlpatterns = [
    #         path("", self.list_view),
    #         path("<int:pk>/", self.detail_view),
    #     ]
    #     return urlpatterns

    def list_view(self, request):
        queryset = self.model.objects.all()
        data = self.get_serializer(queryset, many=True).data
        return JsonResponse(data, safe=False)

    def detail_view(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        data = self.get_serializer(obj).data
        return JsonResponse(data)

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)


class JunctionRouter:
    junction_model = None
    left_model = None
    right_model = None
    base_name = None

    def __init__(self):
        self.base_name = self.base_name or self.junction_model.__name__.lower()

    def get_urls(self):
        urlpatterns = [
            path("", self.list_view),
            path("<int:pk>/", self.detail_view),
            path("<int:pk>/left/", self.left_view),
            path("<int:pk>/right/", self.right_view),
        ]
        return urlpatterns

    def list_view(self, request):
        queryset = self.junction_model.objects.all()
        data = self.get_serializer(queryset, many=True).data
        return JsonResponse(data, safe=False)

    def detail_view(self, request, pk):
        obj = self.junction_model.objects.get(pk=pk)
        data = self.get_serializer(obj).data
        return JsonResponse(data)

    def left_view(self, request, pk):
        obj = self.junction_model.objects.get(pk=pk)
        data = self.get_serializer(obj.left).data
        return JsonResponse(data)

    def right_view(self, request, pk):
        obj = self.junction_model.objects.get(pk=pk)
        data = self.get_serializer(obj.right).data
        return JsonResponse(data)

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)
