from django.db import models, transaction



class Proiect(models.Model):
    object = None
    id_proiect = models.BigAutoField(db_column='ID_Proiect', primary_key=True)  # Field name made lowercase.
    nume = models.CharField(db_column='Nume', max_length=45)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.
    tip = models.CharField(db_column='Tip', max_length=45)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_date', blank=True, null=True)  # Field name made lowercase.
    finish_date = models.DateField(db_column='Finish_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proiecte'
        verbose_name = 'Proiect'
        verbose_name_plural = 'Proiecte'
        ordering = ['nume']

    def __str__(self):
        return self.represent

    @property
    def represent(self):
        return F'{self.nume}'

    def create(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update(self):
        with transaction.atomic():
            self.save(force_update=True)

    def remove(self):
        with transaction.atomic():
            self.delete()