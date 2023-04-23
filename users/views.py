from django.db.models import Count, Q
from rest_framework.generics import (
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    RetrieveAPIView
)

from users.models import User
from users.serializers import (
    UserListSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserDestroySerializer,
    UserRetrieveSerializer
)


class UserListView(ListAPIView):
    queryset = User.objects.prefetch_related('locations').annotate(
        total_ads=Count('ads', filter=Q(ads__is_published=True))).order_by('username')
    serializer_class = UserListSerializer

    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #     paginator = Paginator(users, settings.TOTAL_PER_PAGE)
    #     page_number = request.GET.get('page')
    #     pag_object = paginator.get_page(page_number)
    #
    #     list(map(lambda user: setattr(user, 'total_ads', user.count_ads if user.count_ads else None), pag_object))
    #
    #     response = {
    #         'items': UserListSerializer(pag_object, many=True).data,
    #         'total': paginator.count,
    #         'num_pages': paginator.num_pages
    #     }
    #
    #     return JsonResponse(response, safe=False)


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.prefetch_related('locations').annotate(
        total_ads=Count('ads', filter=Q(ads__is_published=True))).order_by('username')
    serializer_class = UserRetrieveSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
