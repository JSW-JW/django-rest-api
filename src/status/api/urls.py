from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (StatusAPIView,
                    StatusDetailAPIView,)

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<int:id>/', StatusDetailAPIView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Start with
# /api/status/ -> List
# /api/status/create -> Create
# /api/status/12/ -> Detail
# /api/status/12/update -> Update
# /api/status/12/delete -> Delete


#End with

# /api/status/ -> List -> CRUD
# /api/status/1 -> Detail -> CRUD


# Final

# /api/status/ -> CRUD & LS
