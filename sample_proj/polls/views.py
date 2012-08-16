from datafilters.views import FilterFormMixin
from datafilters.decorators import filter_powered

from django.views.generic import ListView
from django.template.response import TemplateResponse

from polls.filters import PollsFilterForm
from polls.models import Poll


class PollListView(FilterFormMixin, ListView):
    model = Poll
    filter_form_cls = PollsFilterForm
    context_object_name = 'polls'

class_based_poll_list = PollListView.as_view()


@filter_powered(PollsFilterForm, queryset_name='polls')
def poll_list(request):
    return TemplateResponse(request,
                            'polls/poll_list.html',
                            {'polls': Poll.objects.all()})
