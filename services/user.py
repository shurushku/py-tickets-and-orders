from django.contrib.auth import get_user_model

from db.models import User


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
) -> None:
    get_user_model().objects.create_user(
        username=username,
        password=password,
        email=email if isinstance(email, str) else "",
        first_name=first_name if isinstance(first_name, str) else "",
        last_name=last_name if isinstance(first_name, str) else "",
    )


def get_user(user_id: int) -> User:
    return get_user_model().objects.get(id=user_id)


def get_user_by_username(username: str) -> User:
    return get_user_model().objects.get(username=username)


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
) -> None:
    user = get_user(user_id)

    if username:
        user.username = username
    if password:
        user.set_password(password)
    if isinstance(email, str):
        user.email = email
    if isinstance(first_name, str):
        user.first_name = first_name
    if isinstance(last_name, str):
        user.last_name = last_name

    user.save()