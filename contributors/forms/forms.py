from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout
from django import forms
from django.utils.translation import gettext_lazy as _


class TableSortSearchForm(forms.Form):
    """A search form."""

    search = forms.CharField(label=False, required=False)
    sort = forms.CharField(
        label=False, widget=forms.HiddenInput(), required=False,
    )
    labels = forms.CharField(
        label=False, widget=forms.HiddenInput(), required=False,
    )

    @property
    def helper(self):
        """Control form attributes and its layout."""
        helper = FormHelper()
        helper.form_method = 'get'
        helper.form_class = 'd-flex'
        helper.layout = Layout(
            Field('sort'),
            Field('labels'),
            FieldWithButtons(
                Field('search', placeholder=_("Filter by name")),
                StrictButton(
                    _("Search"),
                    type='submit',
                    css_class='btn btn-outline-primary',
                ),
            ),
        )
        return helper


class CombinedSearchForm(TableSortSearchForm):
    """Search form of contributors by organization."""

    organizations = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(),
    )

    @property
    def helper(self):
        """Control form attributes and its layout."""
        helper = FormHelper()
        helper.form_method = 'get'
        helper.form_class = 'd-flex'
        helper.layout = Layout(
            Field('search', placeholder=_("Filter by name")),
            FieldWithButtons(
                Field(
                    'organizations', placeholder=_("Filter by organization"),
                ),
                StrictButton(
                    _("Search"),
                    type='submit',
                    css_class='btn btn-outline-primary',
                ),
            ),
        )
        return helper


class NameStatusFilterForm(TableSortSearchForm):
    """Search form of issues by their status."""

    status_choices = [
        ('', _('Filter by status')),
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    state = forms.ChoiceField(
        choices=status_choices,
        required=False,
        label=False,
        initial='',
    )

    @property
    def helper(self):
        """Control form attributes and its layout."""
        helper = FormHelper()
        helper.form_method = 'get'
        helper.form_class = 'd-flex'
        helper.layout = Layout(
            Field('search', placeholder=_("Filter by name")),
            FieldWithButtons(
                Field('state'),
                StrictButton(
                    _("Search"),
                    type='submit',
                    css_class='btn btn-outline-primary',
                ),
            ),
        )
        return helper


class PullRequestNameStatusFilterForm(NameStatusFilterForm):
    """Search form of pull requests by their status."""

    status_choices = [
        ('', _('Filter by status')),
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('merged', 'Merged'),
    ]

    state = forms.ChoiceField(
        choices=status_choices,
        required=False,
        label=False,
        initial='',
    )
