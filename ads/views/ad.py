import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView

from avito import settings
from users.models import User
from ads.models import Category, Ad


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        users = self.object_list.select_related('author').select_related('category').order_by('-price', 'name').all()
        paginator = Paginator(users, settings.TOTAL_PER_PAGE)
        page_number = request.GET.get('page')
        pag_object = paginator.get_page(page_number)

        items = []
        for ad in pag_object:
            items.append({
                'id': ad.pk,
                'name': ad.name,
                'author_id': ad.author.id,
                'author': ad.author.username,
                'price': ad.price,
                'description': ad.description,
                'image': ad.image.url,
                'is_published': ad.is_published,
                'category_id': ad.category.id,
                'category': ad.category.name
            })

        response = [{
            'items': items,
            'total': paginator.count,
            'num_pages': paginator.num_pages
        }]

        return JsonResponse(response, status=200, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = [
        'name',
        'author',
        'price',
        'description',
        'image',
        'is_published',
        'category'
    ]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        author = get_object_or_404(User, pk=ad_data.get('author'))
        category = get_object_or_404(Category, pk=ad_data.get('category'))

        ad, created = Ad.objects.get_or_create(
            name=ad_data.get('name'),
            defaults={
                'author': author,
                'price': ad_data.get('price'),
                'description': ad_data.get('description'),
                'image': ad_data.get('image'),
                'is_published': ad_data.get('is_published'),
                'category': category
            })

        return JsonResponse({
            'id': ad.pk,
            'name': ad.name,
            'author_id': ad.author.id,
            'author': ad.author.username,
            'price': ad.price,
            'description': ad.description,
            'image': ad.image.url,
            'is_published': ad.is_published,
            'category_id': ad.category.id,
            'category': ad.category.name
        }, status=201)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ad = self.get_object()

        return JsonResponse({
            'id': ad.pk,
            'name': ad.name,
            'author_id': ad.author.id,
            'author': ad.author.username,
            'price': ad.price,
            'description': ad.description,
            'image': ad.image.url,
            'is_published': ad.is_published,
            'category_id': ad.category.id,
            'category': ad.category.name
        }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = [
        'name',
        'price',
        'description',
        'image',
    ]

    def patch(self, request, *args, **kwargs):
        ad = self.get_object()
        ad_data = json.loads(request.body)

        if 'name' in ad_data:
            ad.name = ad_data.get('name')
        if 'description' in ad_data:
            ad.description = ad_data.get('description')
        if 'price' in ad_data:
            ad.price = ad_data.get('price')
        if 'image' in ad_data:
            ad.image = ad_data.get('image')

        ad.save()

        return JsonResponse({
            'id': ad.pk,
            'name': ad.name,
            'author_id': ad.author.id,
            'author': ad.author.username,
            'price': ad.price,
            'description': ad.description,
            'image': ad.image.url,
            'is_published': ad.is_published,
            'category_id': ad.category.id,
            'category': ad.category.name
        }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UploadImageView(UpdateView):
    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):
        ad = self.get_object()
        file = request.FILES.get('image')

        if file:
            ad.image = file

        ad.save()

        return JsonResponse({
            'id': ad.pk,
            'name': ad.name,
            'author_id': ad.author.id,
            'author': ad.author.username,
            'price': ad.price,
            'description': ad.description,
            'image': ad.image.url,
            'is_published': ad.is_published,
            'category_id': ad.category.id,
            'category': ad.category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            'status': 'ok'
        }, status=204)
