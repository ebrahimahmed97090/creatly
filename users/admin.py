from django.contrib import admin
from users.models import UserProfileInfo, PaymentMethods, WebSites, WebsiteOptions, Pages, Elements, ElementAttributes, \
    ElementClasses

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(PaymentMethods)
admin.site.register(WebSites)
admin.site.register(WebsiteOptions)
admin.site.register(Pages)
admin.site.register(Elements)
admin.site.register(ElementAttributes)
admin.site.register(ElementClasses)
