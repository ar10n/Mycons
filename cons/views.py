from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Contract


class HomePageView(TemplateView):
    template_name = 'cons/index.html'


class SearchResultView(ListView):
    model = Contract
    template_name = 'cons/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Contract.objects.filter(
            Q(company_name__icontains=query) | Q(
                notice_number__icontains=query)
        )
        return object_list
