# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from models import Audio
from redpanal.project.models import Project
from redpanal.core.forms import TagField
from redpanal.utils.helpers import get_file_extension

AUDIO_EXTENSIONS = ["mp3", "ogg", "oga", "flac"]

class AudioForm(forms.ModelForm):


    tags = TagField(required=False)
    project = forms.ModelChoiceField(Project)
    audio = forms.FileField(label=_("Audio"), help_text=_("Allowed extensions: %s") % ", ".join(AUDIO_EXTENSIONS))

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.add_input(Submit('submit', 'Submit'))
    class Meta:
        model = Audio
        widgets = {
            'license': forms.RadioSelect,
        }

    def __init__(self, data=None, *args, **kwargs):
        user = kwargs.pop('user')
        super(AudioForm, self).__init__(data, *args, **kwargs)
        self.instance.user = user
        initial_project = self.instance.project_set.all()[0] if self.instance.pk and \
                         self.instance.project_set.all() else None
        self.fields['project'] = forms.ModelChoiceField(queryset=Project.objects.filter(user=user),
                                                        initial=initial_project)

    def clean_audio(self):
        f = self.cleaned_data.get('audio', False)
        uploading_new_file = isinstance(f, SimpleUploadedFile)

        if not uploading_new_file:
            return f
        if not f:
            raise ValidationError(_("Couldn't read uploaded file"))
        if "audio" not in f.content_type:
            raise ValidationError(_("Invalid audio file Content-Type '%s'") % f.content_type)
        if not get_file_extension(f.name) in AUDIO_EXTENSIONS:
            raise ValidationError(_("Invalid audio file extension"))
        return f
