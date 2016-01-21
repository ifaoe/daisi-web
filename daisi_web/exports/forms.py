from django import forms


class ExportForm(forms.Form):
    export_session = forms.CharField(label='Projektname', widget=forms.TextInput(
            attrs={'id': 'filter_input', 'auto': 'projects', 'placeholder': 'Project'}))
    export_type_choices = (
        ('bsh', 'BSH-Export'),
        # ('view_census', 'Rohdaten-Export'),
        ('daisi_qa_wrong_image', 'QA - falsche Bildnummer'),
        ('daisi_qa_double_mark', 'QA - Doppelmarkierungen'),
        ('daisi_qa_double_anthro', 'QA - Doppelmarkierungen (ANTHRO)'),
    )
    export_format_choices = (
        # ('csv', 'CSV'),
        ('xlsx', 'Excel'),
        # ('html', 'HTML'),
    )
    export_type = forms.ChoiceField(label='Exporttyp', widget=forms.RadioSelect, choices=export_type_choices, initial='bsh')
    export_format = forms.ChoiceField(label='Dateiformat', widget=forms.RadioSelect, choices=export_format_choices, initial='xlsx')

