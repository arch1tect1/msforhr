import uuid
import os
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from .utils import auto_delete_filefields_on_delete


class File(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='documents/')

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super(File, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title


class BaseModel(models.Model):
    """
    Base class for all models;
    defines common metadata
    """
    class Meta:
        abstract = True
        ordering = ('-created', )  # better choice for UI
        get_latest_by = "-created"

    # Primary key
    id = models.UUIDField('id', default=uuid.uuid4, primary_key=True, unique=True,
        null=False, blank=False, editable=False)

    # metadata
    created = models.DateTimeField(_('created'), null=True, blank=True, )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('created by'), null=True, blank=True, related_name='+', on_delete=models.SET_NULL)
    updated = models.DateTimeField(_('updated'), null=True, blank=True, )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('updated by'), null=True, blank=True, related_name='+', on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)

    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %
            (self._meta.app_label, self._meta.model_name), args=(self.id,))

    def get_absolute_url(self):
        return self.get_admin_url()

    def created_display(self):
        return format_datetime(self.created)
    created_display.short_description = _('Created')
    created_display.admin_order_field = 'created'

    def updated_display(self):
        return format_datetime(self.updated)
    updated_display.short_description = _('Updated')
    updated_display.admin_order_field = 'updated'

    def save(self, *args, **kwargs):
        today = timezone.now()
        if self.created is None:
            self.created = today
        self.updated = today
        return super(BaseModel, self).save(*args, **kwargs)
