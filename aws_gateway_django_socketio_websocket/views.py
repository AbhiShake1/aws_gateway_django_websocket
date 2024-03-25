from django.http import JsonResponse
from django_aws_api_gateway_websockets.views import WebSocketView

class SeatSocketView(WebSocketView):
    def post(self, request):
        return JsonResponse({})

    def default(self, request, *args, **kwargs) -> JsonResponse:
        return JsonResponse({"a": "b"})

    def connect(self, request, *args, **kwargs):
        print('connected')
        return super().connect(request, *args, **kwargs)

    def select(self, request, *args, **kwargs):
        print('selected')
        return JsonResponse({"id": str(self.websocket_session), "status": "selected"})

    def unselect(self, request, *args, **kwargs):
        print('unselected')
        return JsonResponse({"id": str(self.websocket_session), "status": "unselected"})

