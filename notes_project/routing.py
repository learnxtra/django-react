from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import notes.routing

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
    URLRouter(
      notes.routing.websocket_urlpatterns
    )
  )
})