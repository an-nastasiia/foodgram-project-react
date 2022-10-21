from rest_framework import mixins, permissions, viewsets
from rest_framework.pagination import (LimitOffsetPagination,
                                       PageNumberPagination)


class CreateDestroyViewSet(mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateListDestroyViewSet(CreateDestroyViewSet,
                               mixins.ListModelMixin,
                               viewsets.GenericViewSet):
    pass