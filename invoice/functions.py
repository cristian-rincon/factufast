from django.conf import settings
from django.core.mail import EmailMessage


def emailInvoiceClient(to_email, from_client, filepath):
    from_email = settings.EMAIL_HOST_USER
    subject = "[Factufast] Invoice Notification"
    body = """
    Good day,

    Please find attached invoice from {} for your immediate attention.

    regards,
    Factufast Online Learning
    """.format(
        from_client
    )

    message = EmailMessage(subject, body, from_email, [to_email])
    message.attach_file(filepath)
    message.send()
