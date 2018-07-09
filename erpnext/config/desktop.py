# coding=utf-8

from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Project",
			"_doctype": "Project",
			"color": "#8e44ad",
			"icon": "octicon octicon-rocket",
			"type": "link",
			"link": "List/Project"
		},
		{
			"module_name": "hr",
			"color": "#2ecc71",
			"icon": "octicon octicon-organization",
			"label": _("Human Resources"),
			"type": "module",
			"hidden": 1
		},
		{
			"module_name": "Projects",
			"color": "#8e44ad",
			"icon": "octicon octicon-rocket",
			"type": "module",
			"hidden": 1
		}
	]
