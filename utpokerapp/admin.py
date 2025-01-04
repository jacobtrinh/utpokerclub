from django.contrib import admin

# Register your models here.

from .models import Home_Game
from .models import Host
from .models import Contact

admin.site.register(Host)
admin.site.register(Home_Game)
admin.site.register(Contact)
