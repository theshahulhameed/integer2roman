from django.views.generic import TemplateView
from .utils import integerToRoman


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.GET.get('integer'):
            try:
                integer = int(self.request.GET.get('integer'))
            except ValueError as error:
                data['error'] = 'Enter an integer input, try again.'
            else:
                try:
                    data['romannumeral'] = integerToRoman(integer)
                    data['integer'] = integer
                except ValueError as error:
                    data['error'] = error
        return data



