from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import Laan

## forms.py lager skjemaet vi benytter oss av når brukeren skal skrive inn sin lånedata.

class Laaneskjema(ModelForm):
    class Meta:
        model = Laan
        fields = ['laanebelop', 'nominellRente', 'terminGebyr', 'utlopsDato', 'saldoDato', 'datoForsteInnbetaling']
        labels = {
            'laanebelop': _('Lånebeløp'),
            'nominellRente': _('Nominell Rente'),
            'terminGebyr': _('Gebyr'),
            'utlopsDato': _('Utløpsdato (YYYY-MM-DD)'),
            'saldoDato': _('Saldodato (YYYY-MM-DD)'),
            'datoForsteInnbetaling': _('Første innbetalingsdato (YYYY-MM-DD)')
        }
