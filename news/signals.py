
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .views import addpost
from django.db.models.signals import post_save, m2m_changed
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post

@receiver(m2m_changed, sender=Post.postCategory.through)
def notify(sender, instance, action, **kwargs):
    if action == "post_add":
        ca = []
        newtitle = instance.title
        newtext = instance.text
        categs = instance.postCategory
        for categ in categs.all():
            for sub in categ.subscribers.all():
                print(sub.username)
                if sub not in ca:
                    ca.append(sub)
                    username = sub.username
                    id = instance.id
                    html = render_to_string(
                        'new_post.html', {'newtitle': newtitle, 'newtext': newtext, 'username':username, 'id':id}
                    )
                    ca.append(sub)
                    msg = EmailMultiAlternatives(
                        subject=f'{newtitle}',
                        body=f'Привет, {sub.username}',
                        from_email='testza1@yandex.ru',
                        to=[f'{sub.email}'],
                        )
                    msg.attach_alternative(html, "text/html")
                    msg.send()
