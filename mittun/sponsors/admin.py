from django.contrib import admin

from mittun.sponsors.models import Sponsor, Category, Contact, Job, Requirement, Responsibility, Bonus


class ContactInline(admin.TabularInline):
    model = Contact


class ContactAdmin(admin.ModelAdmin):
    pass


class SponsorAdmin(admin.ModelAdmin):

    inlines = [
        ContactInline,
    ]

class RequirementInline(admin.TabularInline):
    model = Requirement

class ResponsibilityInline(admin.TabularInline):
    model = Responsibility

class BonusInline(admin.TabularInline):
    model = Bonus

class JobAdmin(admin.ModelAdmin):
    inlines = [
        RequirementInline,
        ResponsibilityInline,
        BonusInline,
    ]

if Contact not in admin.site._registry:
    admin.site.register(Contact, ContactAdmin)

if Sponsor not in admin.site._registry:
    admin.site.register(Sponsor, SponsorAdmin)

if Category not in admin.site._registry:
    admin.site.register(Category)

if Job not in admin.site._registry:
    admin.site.register(Job, JobAdmin)

if Responsibility not in admin.site._registry:
    admin.site.register(Responsibility)

if Requirement not in admin.site._registry:
    admin.site.register(Requirement)

if Bonus not in admin.site._registry:
    admin.site.register(Bonus)

