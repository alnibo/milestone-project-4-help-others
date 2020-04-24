from django.conf.urls import url, include
from accounts.views import logout, login, register, user_profile, donation_history
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^profile/', user_profile, name="profile"),
    url(r"^donation_history/", donation_history, name="donation_history"),
    url(r'^password-reset/', include(url_reset))
]
