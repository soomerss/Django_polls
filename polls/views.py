import logging

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .models import Choice, Question

logger = logging.getLogger(__name__)

# Create your views here.


class PollsListView(ListView):
    template_name = "polls/index.html"
    model = Question


class PollsDetailView(DetailView):
    template_name = "polls/detail.html"
    model = Question


def vote(request, pk):
    logger.debug(f"vote().question_id: {pk}")
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            context={
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(pk,)))


class ResultsView(DetailView):
    model = Question
    template_name = "polls/results.html"
