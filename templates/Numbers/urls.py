from django.urls import path
from . import views
urlpatterns=[
	path('round-to-half',views.r2),
    path('round-to-one-fourth',views.r4),
    path('round-to-one-eighth',views.r8),
    path('round-to-one-by-16',views.r16),
    path('round-to-one-by-32',views.r32),
    path('round-to-one-by-64',views.r64),
    path('round-to-nearest-billionth',views.billionth),
    path('round-to-nearest-ten-billionth',views.billionth10),
    path('round-to-nearest-hundred-billionth',views.billionth100),
    path('round-to-nearest-trillionth',views.trillionth),
    path('round-to-nearest-ten-trillionth',views.trillionth10),
    path('round-to-nearest-hundred-trillionth',views.trillionth100),
    path('round-to-nearest-quadrillionth',views.quadrillionth),
    path('round-to-nearest-ten-quadrillionth',views.quadrillionth10),
    path('round-to-nearest-hundred-quadrillionth',views.quadrillionth100),
]

