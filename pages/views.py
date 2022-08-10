from django.views.generic import TemplateView, RedirectView


# class HomePageView(TemplateView):
#     template_name = "home.html"


# tmp:
class HomePageView(RedirectView):
    pattern_name = "article_list"

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
