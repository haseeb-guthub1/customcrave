from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/meals/", include("meals.urls")),   # ✅ Make sure this is here
    path("api/budget/", include("budget.urls")),
    path("api/scraper/", include("scraper.urls")),
    path("api/chatbot/", include("chatbot.urls")),
]
