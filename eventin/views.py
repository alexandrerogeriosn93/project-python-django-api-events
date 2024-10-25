from django.http import JsonResponse

def participants(request):
    match request.method:
        case "GET":
            participant = {
                "id": 1,
                "name": "Alexandre Rogério"
            }

            return JsonResponse(participant)


