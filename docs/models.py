from django.db import models

# Create your models here.


class Doc(models.Model):
    doc_id = models.IntegerField(primary_key=True)
    doc_title = models.CharField(max_length=100)
    doc_text = models.TextField()
    doc_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doc_name


class DocSection(models.Model):
    doc_id = models.ForeignKey(Doc, on_delete=models.CASCADE)
    doc_section_id = models.IntegerField(primary_key=True)
    doc_section_title = models.CharField(max_length=100)
    doc_section_text = models.TextField()
    doc_section_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doc_section_name
