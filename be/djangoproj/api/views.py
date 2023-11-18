from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from django.core.serializers import serialize
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import User
from django.db.models import Q
from .forms import UserForm


import json


@method_decorator(csrf_exempt, name="dispatch")
class FilteredUserIds(View):
    def get(self, request):
        q_filter = Q()
        search_input = request.GET.get("search")
        if search_input:
            q_filter |= Q(name__icontains=search_input)
            q_filter |= Q(address__icontains=search_input)
        users = User.objects.filter(q_filter)
        ids = list(users.values_list("id", flat=True))
        return JsonResponse({"results": ids}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class UserList(View):
    def get(self, request):
        users = User.objects.all()
        serialized_users = list(users.values())
        return JsonResponse({"results": serialized_users}, safe=False)

    @csrf_exempt
    def post(self, request):
        form = UserForm(json.loads(request.body))
        if form.is_valid():
            user = form.save()
            user_data = {
                "id": user.id,
                "name": user.name,
                "address": user.address,
            }
            return JsonResponse({"results": user_data}, status=201)
        errors = {"errors": form.errors}
        return JsonResponse(errors, status=400)


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    model = User

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        data = {
            "message": f"Successfully deleted {str(self.object.name)}",
        }
        return JsonResponse(data)
