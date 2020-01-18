from setuptools import setup, find_packages

from cmsplugin_contact_form import __version__

setup(
    name='cmsplugin-contact-form',
    version=__version__,
    description='A Django CMS plugin to create functional contact forms.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    maintainer='Julia Rizza',
    maintainer_email='contato@juliarizza.com',
    url='https://github.com/juliarizza/djangocms_contact_form',
    license='MIT',
    keywords='django djangocms plugin form contact email',
    packages=['cmsplugin_contact_form'],
    package_dir={'cmsplugin_contact_form': 'cmsplugin_contact_form'},
    package_data={'cmsplugin_contact_form': [
        'templates/cmsplugin_contact_form/*.html']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
