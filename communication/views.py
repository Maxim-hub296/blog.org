import json

from django.db import IntegrityError
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.core.mail import send_mail

from communication.models import Address


# Create your views here.

class FeedbackTemplateView(TemplateView):
    template_name = "communication/feedback.html"

class NewsletterTemplateView(TemplateView):
    template_name = "communication/newsletter_form.html"

class SendQuestionTemplateView(TemplateView):
    template_name = "communication/question_form.html"




def send_question(request):
    if request.method == "POST":
        data = json.loads(request.body)
        sender_mail = data["sender_mail"]
        subject = "По поводу исследования"
        question = data["question"]

        send_mail(subject, question, sender_mail, ["maxsavikin@gmail.com"])
        return JsonResponse({"message": "Вас успешно отправлен! Ожидайте ответа, я не заставлю долго ждать ;)"})
    return JsonResponse({"error": "Метод не поддерживается"}, status=405)



def add_to_newsletter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data["email"]
        try:
            address = Address.objects.create(email=email)
            address.save()
            print(address)
            return JsonResponse({"message": "Вы успешно подписались на рассылку"})
        except IntegrityError:
            return JsonResponse({"message": "Вы уже подписаны на рассылку"})


def del_from_newsletter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data["email"]
        address = Address.objects.get(email=email)
        if address:
            address.delete()
        return JsonResponse({"message": "Вы отписались от рассылки"})
