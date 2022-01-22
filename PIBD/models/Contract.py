from django.db import models, transaction

from PIBD.models import Client, Proiect


class Contract(models.Model):
    id_contract = models.BigAutoField(db_column='ID_Contract', primary_key=True)  # Field name made lowercase.
    client = models.ForeignKey(Client, models.CASCADE, db_column='ID_Client')  # Field name made lowercase.
    proiect = models.ForeignKey(Proiect, models.CASCADE, db_column='ID_Proiect')  # Field name made lowercase.
    team_name = models.CharField(db_column='Team_name', max_length=45)  # Field name made lowercase.
    urgent = models.CharField(db_column='Urgent', max_length=2, blank=True, null=True)  # Field name made lowercase.
    deadline = models.DateField(db_column='Deadline')  # Field name made lowercase.
    pret = models.BigIntegerField(db_column='Pret')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contracte'
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracte'
        ordering = ['team_name', 'urgent']

    def __str__(self):
        return self.represent

    @property
    def represent(self):
        return F'{self.proiect.nume} - {self.client.nume} ({self.client.prenume}) {self.client.cnp} '

    def create(self):
        with transaction.atomic():
            self.save(force_insert=True)

    def update(self):
        with transaction.atomic():
            self.save(force_update=True)

    def remove(self):
        with transaction.atomic():
            self.delete()