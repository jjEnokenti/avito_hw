import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView

from avito import settings
from users.models import User, Location
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
        data = json.loads(request.body)

        locations = data.get('locations')

        user = User.objects.create(
            username=data.get('username'),
            password=data.get('password'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            role=data.get('role'),
            age=data.get('age')
        )

        for location in locations:
            loc, created = Location.objects.get_or_create(
                name=location
            )
            user.locations.add(loc)

        user.save()

        return JsonResponse(UserCreateSerializer(user).data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['username']

    def patch(self, request, *args, **kwargs):
        data = json.loads(request.body)

        user = self.get_object()
        locations = data.get('locations')

        if 'password' in data:
            user.password = data.get('password')
        if 'first_name' in data:
            user.first_name = data.get('first_name')
        if 'last_name' in data:
            user.last_name = data.get('last_name')
        if 'role' in data:
            user.role = data.get('role')
        if 'age' in data:
            user.age = data.get('age')
        if 'locations' in data:
            for location in locations:
                loc, created = Location.objects.get_or_create(
                    name=location
                )
                user.locations.add(loc)

        user.save()

        return JsonResponse(UserUpdateSerializer(user).data, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            'status': 'ok'
        })
