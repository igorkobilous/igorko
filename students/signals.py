# -*- coding: utf-8 -*-
import logging

from django.db.models.signals import post_save, post_delete
from django.core.signals import request_started
from django.dispatch import receiver

from .models import Student, Group, Exam


@receiver(post_save)
def log_student_group_exam_update_added_event(sender, **kwargs):
	"""Writes information about newly added or update student into log file"""
	logger = logging.getLogger(__name__)
	if sender == Student:
		student = kwargs['instance']
		if kwargs['created']:
			logger.info("Student added: %s %s (ID: %d)", 
				student.first_name, student.last_name, student.id)
		else:
			logger.info("Student update: %s %s (ID: %d)",
				student.first_name, student.last_name, student.id)
	elif sender == Group:
		group = kwargs['instance']
		if kwargs['created']:
			logger.info("Group added: %s (ID: %d)", 
				group.title, group.id)
		else:
			logger.info("Group update: %s (ID: %d)",
				group.title, group.id)
	elif sender == Exam:
		exam = kwargs['instance']
		if kwargs['created']:
			logger.info("Exam added: %s (ID: %d)", 
				exam.subject, exam.id)
		else:
			logger.info("Exam update: %s (ID: %d)",
				exam.subject, exam.id)

@receiver(post_delete)
def log_student_group_exam_deleted_event(sender, **kwargs):
	"""Writes information about deleted student into log file"""
	logger = logging.getLogger(__name__)
	if sender == Student:
		student = kwargs['instance']
		logger.info("Student deleted: %s %s (ID: %d)", student.first_name,
			student.last_name, student.id)
	elif sender == Group:
		group = kwargs['instance']
		logger.info("Group deleted: %s (ID: %d)", group.title, group.id)
	elif sender == Exam:
		exam = kwargs['instance']
		logger.info("Exam deleted: %s (ID: %d)", exam.subject, exam.id)

@receiver(request_started)
def my_callback(sender, **kwargs):
	print('request_started')