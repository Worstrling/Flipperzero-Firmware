from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.object.filter(user=request.user)

    if not request.session.session_key:
        request.session.create()
    return Cart.object.filter(session_key=request.session.session_key)