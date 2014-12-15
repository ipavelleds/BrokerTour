from django.contrib import admin
from landing.models import Tour, Proposal


class ProposalAdmin(admin.ModelAdmin):
    list_display = ('tour', 'phone', 'name', 'email')

admin.site.register(Tour)
admin.site.register(Proposal, ProposalAdmin)