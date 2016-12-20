

def add_owner_as_membership(sender, instance, created, **kwargs):
    if created:
        instance.memberships.create(user=instance.owner, role=2)
