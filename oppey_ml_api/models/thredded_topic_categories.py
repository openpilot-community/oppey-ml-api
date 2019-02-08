from django.db import models


class ThreddedTopicCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    topic_id = models.BigIntegerField()
    category_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'thredded_topic_categories'
