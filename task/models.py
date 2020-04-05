from django.db import models

STATUS = ((0, "Undone"), (1, "Done"))

class TaskModel(models.Model):
	task = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add = True)
	complete = models.IntegerField(choices = STATUS, default=0)

	class Meta:
		ordering = ["-created_at",]

	def __str__(self):
		return self.task