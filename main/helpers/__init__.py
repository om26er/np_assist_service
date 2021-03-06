import random
import threading

from django.conf import settings
from django.core.mail import send_mail


def generate_random_key():
    # Ensures the return number is always 5 numbers long.
    return random.randint(10000, 99999)


def _send_account_activation_email(email, activation_key):
    send_mail(
        'NP Assist: Account activation',
        'Account activation key: {}'.format(activation_key),
        settings.EMAIL_HOST_USER,
        [str(email)],
        fail_silently=False)


def send_account_activation_email(email, key):
    thread = threading.Thread(
        target=_send_account_activation_email, args=(email, key))
    thread.start()
