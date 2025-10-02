from django.urls import path

from . import views

app_name = "communication"

urlpatterns = [
    path("news_letter/", views.NewsletterTemplateView.as_view(), name="news_letter"),
    path("subscribe/", views.add_to_newsletter, name="subscribe"),
    path("unsubscribe/", views.del_from_newsletter, name="unsubscribe"),
    path("ask_question/", views.SendQuestionTemplateView.as_view(), name="ask_question"),
    path("send_question/", views.send_question, name="send_question"),
    path("feedback/", views.FeedbackTemplateView.as_view(), name="feedback"),
]