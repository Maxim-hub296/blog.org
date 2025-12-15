from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Story
from communication.models import Address


@receiver(post_save, sender=Story)
def story_story_save(sender, instance: Story, created, **kwargs):
    if created:
        print("Пишем письмо")
        emails = list(Address.objects.values_list('email', flat=True))
        send_mail(
            "Новая история на romantic.blog",
            f"""Доброго времени суток! С большим удовольствием сообщаю вам, что я опубликовал новую историю {instance.title}! С нетерпением жду вашего прочтения и нашей дальнейшей беседы. Если вы хотите отписаться от рассылки то зайдите на сайт в раздел "Рассылка". Всего хорошего!""",
            "maxsavikin@gmail.com",
            emails,
            fail_silently=False
        )
        print("Письмо")
