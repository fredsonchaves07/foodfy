from threading import Thread

from app.ext.mail import mail
from flask import current_app, render_template
from flask_mail import Message


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()

    msg = Message(
        "[Foodfy] - " + subject,
        sender="Notificações Foodfy <notifications@foodfy.com",
        recipients=[to],
    )

    msg.html = render_template(template, **kwargs)

    thread = Thread(target=send_async_mail, args=[app, msg])
    thread.start()

    return thread
