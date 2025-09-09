# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.db.models import F
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    # return HttpResponse(template.render(context, request)) insted of this django has a shortcut
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # either u can use this below one 
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question}) # or u can use this below one

# def detail(request, question_id):                 
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})             
    # render will take 1- request object 2- template name 3- context dictionary
    
    # return HttpResponse(output)

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})    