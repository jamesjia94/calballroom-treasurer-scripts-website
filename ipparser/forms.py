from django import forms
from formatChecker import ContentTypeRestrictedFileField

MAX_UPLOAD_SIZE = 524288
class IPScheduleForm(forms.Form):
    file = ContentTypeRestrictedFileField(max_upload_size=MAX_UPLOAD_SIZE)