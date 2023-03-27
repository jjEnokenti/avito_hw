from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView

from ads.models import Category, Ad


class MainView(View):

    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


class CategoryView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        categories = self.get_queryset()
        response = []

        for category in categories:
            response.append({
                'id': category.id,
                'name': category.name
            })

        return JsonResponse(response, status=200, safe=False)


class AdView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ads = self.get_queryset()
        response = []

        for ad in ads:
            response.append({
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            })

        return JsonResponse(response, status=200, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse({
            'id': category.id,
            'name': category.name
        }, status=200)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Ad.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published
        }, status=200)
