# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luckdraw.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()





#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line


def main():
    """Run administrative tasks."""
    if sys.platform == "win32":
        bind = "127.0.0.1:" + str(8000)
    else:
        bind = "0.0.0.0:" + str(80)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luckdraw.settings')
    # execute_from_command_line(['', 'runserver', bind, '--nostatic'])
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
