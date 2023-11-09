from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from django.views import View

import json


class ItemList(View):
    def get(self, request):
        items = [
            {"id": 1, "name": "avi"},
            {"id": 2, "name": "david"},
            {"id": 3, "name": "moshe"},
        ]
        return JsonResponse({"results": items}, safe=False)
