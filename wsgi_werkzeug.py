# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import os

from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application
from django.template import TemplateSyntaxError
from django.views import debug
from django.views.debug import technical_500_response
from django_extensions.management.utils import RedirectHandler
from werkzeug.debug import DebuggedApplication


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

logging.getLogger(__name__)

werklogger = logging.getLogger('werkzeug')
werklogger.setLevel(logging.INFO)
werklogger.addHandler(RedirectHandler(__name__))
werklogger.propagate = False


def forward_technical_500_response(request, exc_type, exc_value, tb, **kwargs):
	if request.META['REMOTE_ADDR'] == '127.0.0.1' and exc_type != TemplateSyntaxError:
		raise #pylint: disable=misplaced-bare-raise
	else:
		return technical_500_response(request, exc_type, exc_value, tb, **kwargs)


debug.technical_500_response = forward_technical_500_response


application = DebuggedApplication(StaticFilesHandler(get_wsgi_application()), True)
