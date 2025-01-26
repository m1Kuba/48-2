#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gr48.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()


# <div style="display: flex; justify-content: center; margin-bottom: 20px; margin-top: 20px;">
#     {% for i in max_pages %}
#         <a href="?page={{ i }}{% if request.GET.search %}&search={{ request.GET.search }}{% endif %}{% if request.GET.category %}&category={{ request.GET.category }}{% endif %}{% if request.GET.ordering %}&ordering={{ request.GET.ordering }}{% endif %}" class="btn btn-primary">{{ i }}</a>
#     {% endfor %}
# </div>


# <div style="display: flex; justify-content: center; margin-bottom: 20px; margin-top: 20px;">
#     {% for i in max_pages %}
#     {% if request.GET%}
#         <a href="{{request.get_full_path}}&page={{i}}" class="btn btn-primary">{{i}}</a>
#     {% else %}
#         <a href="/posts/?page" class="btn btn-primary">{{i}}</a>
#     {% endif %}
#     {% endfor %}
# </div>