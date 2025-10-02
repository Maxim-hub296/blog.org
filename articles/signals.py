from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Article
from communication.models import Address


@receiver(post_save, sender=Article)
def after_article_save(sender, instance: Article, created, **kwargs):
    if created:
        print("Пишем письмо")
        emails = list(Address.objects.values_list('email', flat=True))
        send_mail(
            "Новая статья на romantic.org",
            f"""Доброго времени суток! С большим удовольствием сообщаю вам, что я опубликовал новую статью своих исследований "{instance.title}".С нетерпением жду вашего прочтения и нашей дальнейшей беседы. Если вы хотите отписаться от рассылки то зайдите на сайт в раздел "Рассылка". Всего хорошего!""",
            "maxsavikin@gmail.com",
            emails,
            fail_silently=False,
        )
        print("Письмо отправлено")
