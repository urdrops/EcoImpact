from django.http import JsonResponse,HttpResponse


def get_names(request):
    # names = ["Hello", "World"]
    # data = {"names": names}
    # return JsonResponse(data)
    str = "Nastya gey"
    res = HttpResponse(str,content_type="text/plain")
    return res

