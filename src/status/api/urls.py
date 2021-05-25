from django.conf.urls import url
from django.urls import path, include

from .views import (StatusListSearchAPIView,
                    StatusAPIView,
                    StatusDetailAPIView)

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<int:id>/', StatusDetailAPIView.as_view()),
]


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
