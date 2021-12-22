from typing import Optional

from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib.auth import login
from django.contrib.auth import logout
from asgiref.sync import sync_to_async
from django.http.request import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import PasswordResetUrl


@sync_to_async
def get_user_for_auth(username: str, password: str) -> User:
    return authenticate(username=username, password=password)


@sync_to_async
def get_password_reset_url_database(user_id: int) -> PasswordResetUrl:
    return PasswordResetUrl.objects.get(user=user_id)


@sync_to_async
def get_user_by_id(user_id: int) -> User:
    return User.objects.get(id=user_id)


@sync_to_async
def auth_login(request: HttpRequest, user: User) -> None:
    login(request, user)


@sync_to_async()
def auth_logout(request: HttpRequest) -> None:
    logout(request)


async def check_redirect(request: HttpRequest) -> None:
    next_url = request.GET.get("next", None)

    # If theres next url redirect there
    if next_url:
        return redirect(next_url)

    return redirect(reverse("home_page"))


@sync_to_async()
def check_if_username_exist(username: str) -> bool:
    return User.objects.filter(username=username).exists()


@sync_to_async()
def check_if_email_exist(email: str) -> bool:
    return User.objects.filter(email=email).exists()


@sync_to_async
def create_new_user(
    username: str,
    email: str,
    password: str,
    first_name=Optional[str],
    last_name=Optional[str],
) -> None:
    database = User.objects.create_user(
        username,
        email,
        password,
    )
    database.first_name = first_name
    database.last_name = last_name
    database.save()


@sync_to_async
def create_new_reset_database(user) -> PasswordResetUrl:
    database = PasswordResetUrl(user=user)
    database.save()
    return database


async def check_register_form_validity(
    request: HttpRequest,
    username: str,
    email: str,
    password: str,
    confirm_password: str,
) -> bool:
    user = await get_user_for_auth(username, password)
    if user:
        messages.warning(request, "User exists")

    username_exists = await check_if_username_exist(username)
    if username_exists:
        messages.warning(request, "Username Exists")

    email_exists = await check_if_email_exist(email)
    if email_exists:
        messages.warning(request, "Email Exists")

    if confirm_password != password:
        messages.warning(request, "Passwords doesn't match")

    if (
        not user
        and not username_exists
        and not email_exists
        and not confirm_password != password
    ):
        return True
    else:
        return False


@sync_to_async
def send_mail_function(
    email_subject: str, email_reset_message: str, from_sender: str, to_receiver: str
) -> None:
    send_mail(
        email_subject,  # subject
        email_reset_message,  # message
        from_sender,  # from email
        [to_receiver],  # to email
    )
