# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView  # FormView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review


# Create your views here.

# =======    FORM VIEW    =======
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# =======    CREATE VIEW    =======
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


# =======    VIEW    =======
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })
#
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#
#         return render(request, "reviews/review.html", {
#             "form": form
#         })


# ========   TEMPLATE VIEW    =========
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works"
        return context


# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

# ========   LIST VIEW    =========
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # Ratings >= 1:

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gte=1)
    #     return data


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context

# ========   DETAIL VIEW    =========
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review


# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#
#         if form.is_valid():
#             # reviews = Review(user_name=form.cleaned_data['user_name'],
#             #                  review_text=form.cleaned_data['review_text'],
#             #                  rating=form.cleaned_data['rating'])
#             # reviews.save()
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#
#     else:
#         form = ReviewForm()
#
#     return render(request, "reviews/review.html", {
#         "form": form
#     })
