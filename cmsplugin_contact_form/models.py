from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from cms.models import CMSPlugin


@python_2_unicode_compatible
class ContactFormCMS(CMSPlugin):
    smtp_server = models.CharField(
        blank=False,
        max_length=255
    )
    smtp_port = models.CharField(
        blank=False,
        max_length=10
    )
    email = models.CharField(
        blank=False,
        max_length=255
    )
    password = models.CharField(
        blank=False,
        max_length=255
    )
    use_tls = models.BooleanField()
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )

    def __str__(self):
        return self.email


@python_2_unicode_compatible
class ContactFormBaseFieldCMS(CMSPlugin):
    label = models.CharField(
        blank=False,
        max_length=255
    )
    html_id = models.CharField(
        blank=False,
        max_length=50
    )
    html_name = models.CharField(
        blank=False,
        max_length=50
    )
    html_classes = models.CharField(
        blank=True,
        max_length=255
    )

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class ContactFormTextFieldCMS(ContactFormBaseFieldCMS):
    html_placeholder = models.CharField(
        blank=True,
        max_length=255
    )
    default_value = models.CharField(
        blank=True,
        max_length=255
    )
    required = models.BooleanField()


@python_2_unicode_compatible
class ContactFormEmailFieldCMS(ContactFormBaseFieldCMS):
    html_placeholder = models.CharField(
        blank=True,
        max_length=255
    )
    default_value = models.CharField(
        blank=True,
        max_length=255
    )
    required = models.BooleanField()


@python_2_unicode_compatible
class ContactFormPhoneFieldCMS(ContactFormBaseFieldCMS):
    html_placeholder = models.CharField(
        blank=True,
        max_length=255
    )
    phone_pattern = models.CharField(
        blank=True,
        max_length=255
    )
    phone_max_length = models.CharField(
        blank=True,
        max_length=4
    )
    default_value = models.CharField(
        blank=True,
        max_length=255
    )
    required = models.BooleanField()


@python_2_unicode_compatible
class ContactFormTextAreaFieldCMS(ContactFormBaseFieldCMS):
    html_placeholder = models.CharField(
        blank=True,
        max_length=255
    )
    html_rows = models.CharField(
        blank=True,
        max_length=4
    )
    html_cols = models.CharField(
        blank=True,
        max_length=4
    )
    default_value = models.CharField(
        blank=True,
        max_length=255
    )
    required = models.BooleanField()


@python_2_unicode_compatible
class ContactFormCheckboxFieldCMS(ContactFormBaseFieldCMS):
    value = models.CharField(
        blank=False,
        max_length=255
    )
    checked = models.BooleanField()


@python_2_unicode_compatible
class ContactFormSubmitFieldCMS(ContactFormBaseFieldCMS):
    type = models.CharField(
        blank=False,
        max_length=255,
        choices=[
            ('button', 'Button'),
            ('input', 'Input')
        ]
    )