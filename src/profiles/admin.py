from django.contrib import admin
from profiles.models import *
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from .models import profile, userStripe

# Register your models here.





admin.site.register(Track)

class SpeakerAdmin(admin.ModelAdmin):
	list_display = ('name', 'bio',)
	fieldset = (
		("General information", {
	        "fields": ("name", "bio", )
	    }),
	    ("Social media", {
	    	"classes": ("collapse",),
		    "fields": ("twitter", "facebook",), 
		    "description": "Add social media here. Remember!, this data will be available to public."
		})
	)

admin.site.register(Speaker, SpeakerAdmin )

def make_approved(modeladmin, request, queryset):
    queryset.update(status='a')
make_approved.short_description = "Mark selected session(s) as approved"

class SessionAdmin(admin.ModelAdmin):
	list_display = ['title', 'speaker', 'status', ]
	list_display_links = ['title', 'speaker',]
	search_fields = ['title', 'abstract']
	list_filter = ['track__title', 'speaker',]
	ordering = ['title',]
	actions = [make_approved]

def make_approved(self, request, queryset):
    rows_updated = queryset.update(status='a')
    if rows_updated == 1:
        message_bit = "1 session was"
    else:
        message_bit = "%s sessions were" % rows_updated

    self.message_user(request, "%s approved." % message_bit)

admin.site.register(Session, SessionAdmin)
    
class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile

admin.site.register(profile, profileAdmin)

class userStripeAdmin(admin.ModelAdmin):
	class Meta:
		model = userStripe

admin.site.register(userStripe, userStripeAdmin)