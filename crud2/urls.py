
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('owners/', include('owners.urls'))
]
