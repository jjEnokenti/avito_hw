import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView

from avito import settings
from users.models import User
from users.serializers import (
    UserListSerializer,
    UserCreateSerializer,
    UserDetailSerializer,
    UserUpdateSerializer
)


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        users = self.object_list.prefetch_related('locations').annotate(
            count_ads=Count('ads', filter=Q(ads__is_published=True))).order_by('username')

        paginator = Paginator(users, settings.TOTAL_PER_PAGE)
        page_number = request.GET.get('page')
        pag_object = paginator.get_page(page_number)

        list(map(lambda user: setattr(user, 'total_ads', user.count_ads if user.count_ads else None), pag_object))

        response = {
            'items': UserListSerializer(pag_object, many=True).data,
            'total': paginator.count,
            'num_pages': paginator.num_pages
        }

        return JsonResponse(response, safe=False)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        setattr(
            user,
            'total_ads',
            user.ads.filter(is_published=True).count() if user.ads.filter(is_published=True) else None
        )

        return JsonResponse(UserDetailSerializer(user).data, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'first_name', 'password', 'last_name', 'role', 'age', 'locations']

    def post(self, request, *args, **kwargs):
        user = UserCreateSerializer(data=json.loads(request.body))

        if user.is_valid():
            user.save()
        else:
            return JsonResponse(user.errors)

        return JsonResponse(user.data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['username']

    def patch(self, request, *args, **kwargs):
        user = UserUpdateSerializer(self.get_object(), data=json.loads(request.body), partial=True)

        if user.is_valid():
            user.save()
        else:
            return JsonResponse(user.errors)

        return JsonResponse(user.data, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            'status': 'ok'
        })
