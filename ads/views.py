import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView

from ads.models import Category, Ad


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class CategoryView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []

        for category in self.object_list:
            response.append({
                'id': category.id,
                'name': category.name
            })

        return JsonResponse(response, status=200, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)

        category, created = Category.objects.get_or_create(
            name=category_data.get('name')
        )

        return JsonResponse({
            'id': category.id,
            'name': category.name
        }, status=201)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category, updated = Category.objects.update_or_create(
            name=category_data.get('name')
        )

        return JsonResponse({
            'id': category.id,
            'name': category.name
        }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            'status': 'ok'
        }, status=204)


# _________ AD VIEWS ___________ #
class AdView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        response = []

        for ad in self.object_list:
            response.append({
                'id': ad.pk,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            })

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
        author = ad_data.get('author')
        ad, created = Ad.objects.get_or_create(
            name=ad_data.get('name'),
            defaults={
                'author': Ad.objects.get(pk=author),
                'price': ad_data.get('price'),
                'description': ad_data.get('description'),
                'image': ad_data.get('image'),
                'is_published': ad_data.get('is_published'),
                'category': ad_data.get('category'),

            })

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author_id': ad.author.id,
            'price': ad.price,
            'description': ad.description,
            'image': ad.image,
            'is_published': ad.is_published,
            'category': ad.category.id
        }, status=201)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ad = self.get_object()

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published
        }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
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

    def patch(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad, updated = Ad.Objects.update_or_create(
            name=ad_data.get('name'),
            defaults={
                'author': ad_data.get('author'),
                'price': ad_data.get('price'),
                'description': ad_data.get('description'),
                'image': ad_data.get('image'),
                'is_published': ad_data.get('is_published'),
                'category': ad_data.get('category'),

            })

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author_id': ad.author.id,
            'price': ad.price,
            'description': ad.description,
            'image': ad.image,
            'is_published': ad.is_published,
            'category': ad.category.id
        }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            'status': 'ok'
        }, status=204)
