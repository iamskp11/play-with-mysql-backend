import time
from copy import deepcopy
from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import (
    permission_classes,
    authentication_classes
    )
from query.factory import QueryHandler
# Create your views here.


class Execute(APIView):

    def get(self, request, *args, **kwargs):
        try:
            query_language = self.kwargs.get("query_language")
            result = QueryHandler().get_instance(
                query_language=query_language
                ).execute(query=request.data.get("query"))

            response_data = {
                "count_of_rows": len(result),
                "data": result
            }
            return Response(
                data=response_data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                data=str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
