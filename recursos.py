"""
Usar Bootstrap 4 en django:
-Instalar:
    libreria django-crispy-forms (V2023.1)
    libreria crispy-bootstrap4 (V2.1)

Configurar crispy
-Entrar en la carpeta principal del proyecto django y abrir el archivo settings.py
-Agregar INSTALLED_APPS:
    'crispy_forms'
    'crispy_bootstrap4'
-Agregar al archivo settings.py dos variables con el valor bootstrap4:
    CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
    CRISPY_TEMPLATE_PACK = 'bootstrap4'

Para usar crispy en las plantillas debemos poner la siguiente etiqueta en cada template
{% load crispy_forms_tags %}
"""
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

