from django.http import JsonResponse


def get_models(request):
    names = 'Test'
    data = {"names": names}
    return JsonResponse(data)


