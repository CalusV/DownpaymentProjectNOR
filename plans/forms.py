from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Laan

class Laaneskjema(ModelForm):
    class Meta:
        model = Laan
        fields = ['laanebelop', 'nominellRente', 'terminGebyr', 'utlopsDato', 'saldoDato', 'datoForsteInnbetaling']
        labels = {
            'laanebelop': _('Lånebeløp'),
            'nominellRente': _('Nominell Rente'),
            'terminGebyr': _('Gebyr'),
            'utlopsDato': _('Utløpsdato'),
            'saldoDato': _('Saldodato'),
            'datoForsteInnbetaling': _('Første innbetalingsdato')
        }

        def sjekk_belop(self):
            data = self.cleaned_data['laanebelop']
            if data < 0:
                raise ModelForm.ValidationError("Lånemengde kan ikke være mindre enn null.")
            return data