from userinfo.models import User


def __main__(request):
    datamodel = User.objects.all()
