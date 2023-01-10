from django.db import models

CHOICES_SELECTED = [
    ('0', 'No'),
    ('1', 'Yes')
]
class Menu(models.Model):
    name = models.CharField(max_length=100)
    uri = models.SlugField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'

    def __unicode__(self):
        return self.name


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    uri = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def get_parent_ids(self):
        if self.parent:
            return self.parent.get_parent_ids() + [self.parent.id]
        else:
            return []


    def get_margin(self):
        if self.parent:
            print(20 + self.parent.get_margin())
            return 20 + self.parent.get_margin()
        else:
            return 20
    def __unicode__(self):
        return self.name