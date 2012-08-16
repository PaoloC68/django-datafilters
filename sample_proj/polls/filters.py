from datafilters.filterform import FilterForm
from datafilters.specs import (GenericSpec, DateFieldFilterSpec,
    GreaterThanFilterSpec, ContainsFilterSpec,
    GreaterThanZeroFilterSpec)


class PollsFilterForm(FilterForm):
    has_exact_votes = GenericSpec('choice__votes')
    has_choice_with_votes = GreaterThanZeroFilterSpec('choice__votes')
    pub_date = DateFieldFilterSpec('pub_date', label='Date of publishing')
    has_major_choice = GreaterThanFilterSpec('choice__votes', value=50)
    question_contains = ContainsFilterSpec('question')
    choice_contains = ContainsFilterSpec('choice__choice_text')
