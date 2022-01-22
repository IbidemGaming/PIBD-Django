from django.db import transaction
from django.views.generic import TemplateView


from PIBD.models import Client

class ClientPageView(TemplateView):
    template_name = 'ListaClienti.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            clienti = Client.objects.all()
        context['clienti'] = clienti
        print(clienti)

        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('updateClient') is not None:
            with transaction.atomic():
                client = Client.objects.get(id_client = int(self.request.POST.get('Select_client_Update')))

            nume = self.request.POST.get("Nume_update")
            nume = nume if nume != '' else client.nume

            prenume = self.request.POST.get("Prenume_update")
            prenume = prenume if prenume != '' else client.prenume

            cnp = self.request.POST.get("CNP_update")
            cnp = cnp if cnp != '' else client.CNP

            telefon = self.request.POST.get("Telefon_update")
            telefon = telefon if len(str(telefon)) == 13 else client.telefon

            email = self.request.POST.get("Email_update")
            email = email if email != '' else client.EMAIL

            adresa = self.request.POST.get("Adresa_update")
            adresa = adresa if adresa != '' else client.adresa

            client = Client(id_client = client.id_client, nume = nume,
                                      prenume = prenume, cnp = cnp, telefon = telefon,
                                      email = email, adresa = adresa)

            client.update()

        elif self.request.POST.get('deleteClient') is not None:
            with transaction.atomic():
                client = Client.objects.get(id_client=int(self.request.POST.get('Select_client_Delete')))
            client.remove()

        return self.render_to_response(self.get_context_data())
