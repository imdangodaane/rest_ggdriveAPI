from django.db import models
from jsonfield import JSONField

# Create your models here.

# class About(models.Model):
#     kind = models.CharField(max_length=100, default='')
#     user = JSONField()
#     storageQuote = JSONField()
#     importFormats = JSONField()
#     exportFormats = JSONField()
#     maxImportSizes = JSONField()
#     maxUploadSizes = models.FloatField()
#     appInstalled = models.BooleanField(default=False)
#     folderColorPalette = JSONField()
#     teamDriveThemes = models.MultipleChoiceField()

#     class Meta:
#         ordering = ('user',)

class About(models.Model):
    contents = JSONField()