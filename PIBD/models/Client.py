from django.db import models, transaction


class Client(models.Model):
    id_client = models.BigAutoField(db_column='ID_Client', primary_key=True)  # Field name made lowercase.
    cnp = models.CharField(db_column='CNP', unique=True, max_length=13)  # Field name made lowercase.
    nume = models.CharField(db_column='Nume', max_length=45)  # Field name made lowercase.
    prenume = models.CharField(db_column='Prenume', max_length=45)  # Field name made lowercase.
    telefon = models.CharField(db_column='Telefon', max_length=13)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    adresa = models.CharField(db_column='Adresa', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clienti'
        verbose_name = 'Client'
        verbose_name_plural = 'Clienți'
        ordering = ['nume', 'prenume']

    def __str__(self):
        return self.represent

    @property
    def nume_complet(self):
        return F'{self.nume} {self.prenume} '

    @property
    def represent(self):
        return F'{self.nume_complet} ({self.cnp})'

    def create(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update(self):
        with transaction.atomic():
            self.save(force_update=True)

    def remove(self):
        with transaction.atomic():
            self.delete()