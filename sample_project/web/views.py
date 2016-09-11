# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView, View


class ErrorView(View):
	def get(self, request, *args, **kwargs): #pylint: disable=unused-argument
		raise RuntimeError("Error")


home = TemplateView.as_view(template_name='home.html')
error = ErrorView.as_view()
