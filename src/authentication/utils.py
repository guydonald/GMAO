from django.contrib.auth.models import Group

def user_in_group(user, group_name):
    if user.groups.filter(name=group_name).exists():
        return True
    return False