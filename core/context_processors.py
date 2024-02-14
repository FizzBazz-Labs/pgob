from django.contrib.auth.models import Group


def context_admin_group(request):
    admin_group = Group.objects.get_or_create(name='admin')
    return {'admin_group': admin_group[0]}
