from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.core.mail import send_mail, get_connection

from . import models

class ContactFormCMSPlugin(CMSPluginBase):
    model = models.ContactFormCMS
    name = 'Contact Form'
    render_template = 'cmsplugin_contact_form/form.html'
    allow_children = True
    child_classes = [
        'ContactFormTextFieldCMSPlugin',
        'ContactFormEmailFieldCMSPlugin',
        'ContactFormPhoneFieldCMSPlugin',
        'ContactFormTextAreaFieldCMSPlugin',
        'ContactFormCheckboxFieldCMSPlugin',
        'ContactFormRadioFieldCMSPlugin',
        'ContactFormDateFieldCMSPlugin',
        'ContactFormTimeFieldCMSPlugin',
        'ContactFormDateTimeFieldCMSPlugin',
        'ContactFormSubmitFieldCMSPlugin'
    ]

    def render(self, context, instance, placeholder):
        request = context['request']
        if request.method == 'POST':
            message = "New message from your website:\n\n"
            email_field = [
                inst for inst in instance.child_plugin_instances
                if isinstance(inst, models.ContactFormTextFieldCMS)
            ][0]
            email_key = email_field.html_name

            submit_field = [
                inst for inst in instance.child_plugin_instances
                if isinstance(inst, models.ContactFormSubmitFieldCMS)
            ][0]
            submit_key = submit_field.html_name

            for key in request.POST.keys():
                if key in ['csrfmiddlewaretoken', submit_key]:
                    continue

                message += '<b>{k}:</b> {v}\n'.format(
                    k=key.capitalize(),
                    v=request.POST[key]
                )

            send_mail(
                subject="New message from your website",
                message=message,
                html_message=message,
                from_email=request.POST[email_key],
                recipient_list=[instance.email],
                fail_silently=False,
                connection=get_connection(
                    backend='django.core.mail.backends.smtp.EmailBackend',
                    host=instance.smtp_server,
                    port=instance.smtp_port,
                    username=instance.email,
                    password=instance.password,
                    use_tls=instance.use_tls
                )
            )

        context.update({
            'placeholder': placeholder,
            'instance': instance
        })

        return context


class ContactFormTextFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormTextFieldCMS
    name = 'Text Field'
    render_template = 'cmsplugin_contact_form/text_field.html'
    require_parent = True
    parent_classes = ['ContactFormCMSPlugin']


class ContactFormEmailFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormEmailFieldCMS
    name = 'Email Field'
    render_template = 'cmsplugin_contact_form/email_field.html'
    require_parent = True
    parent_classes = ['ContactFormCMSPlugin']


class ContactFormPhoneFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormPhoneFieldCMS
    name = 'Phone Field'
    render_template = 'cmsplugin_contact_form/phone_field.html'
    require_parent = True
    parent_classes = ['ContactFormCMSPlugin']


class ContactFormTextAreaFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormTextAreaFieldCMS
    name = 'Text Area Field'
    render_template = 'cmsplugin_contact_form/textarea_field.html'
    require_parent = True
    parent_classes = ['ContactFormCMSPlugin']


class ContactFormCheckboxFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormCheckboxFieldCMS
    name = 'Checkbox Field'
    render_template = 'cmsplugin_contact_form/checkbox_field.html'
    require_parent = True
    parent_classes = ['ContactFormCMSPlugin']


class ContactFormRadioFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormCheckboxFieldCMS
    name = 'Radio Field'
    render_template = 'cmsplugin_contact_form/radio_field.html'
    require_parent = True
    parent_classes = ['ContactFormCMSPlugin']


class ContactFormDateFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormTextFieldCMS
    name = 'Date Field'
    render_template = 'cmsplugin_contact_form/date_field.html'
    require_parent = True
    parent_classes = ['ContactFormCMSPlugin']


class ContactFormTimeFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormTextFieldCMS
    name = 'Time Field'
    render_template = 'cmsplugin_contact_form/time_field.html'
    require_parent = True
    parent_classes = ['ContactFormCMSPlugin']


class ContactFormDateTimeFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormTextFieldCMS
    name = 'Date & Time Field'
    render_template = 'cmsplugin_contact_form/datetime_field.html'
    require_parent = True
    parent_classes = ['ContactFormCMSPlugin']


class ContactFormSubmitFieldCMSPlugin(CMSPluginBase):
    model = models.ContactFormSubmitFieldCMS
    name = 'Submit Field'
    render_template = 'cmsplugin_contact_form/submit_field.html'
    require_parent = True
    parent_classes = ['ContactFormCMSPlugin']
    

plugin_pool.register_plugin(ContactFormCMSPlugin)
plugin_pool.register_plugin(ContactFormTextFieldCMSPlugin)
plugin_pool.register_plugin(ContactFormEmailFieldCMSPlugin)
plugin_pool.register_plugin(ContactFormPhoneFieldCMSPlugin)
plugin_pool.register_plugin(ContactFormTextAreaFieldCMSPlugin)
plugin_pool.register_plugin(ContactFormCheckboxFieldCMSPlugin)
plugin_pool.register_plugin(ContactFormRadioFieldCMSPlugin)
plugin_pool.register_plugin(ContactFormDateFieldCMSPlugin)
plugin_pool.register_plugin(ContactFormTimeFieldCMSPlugin)
plugin_pool.register_plugin(ContactFormDateTimeFieldCMSPlugin)
plugin_pool.register_plugin(ContactFormSubmitFieldCMSPlugin)