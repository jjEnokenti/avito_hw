from django.http import JsonResponse
from django.views import View


class MainView(View):

    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)
