#PIBD_PROJECT views home_page_view.py

from dateutil.parser import parse
from django.db import transaction
from django.views.generic import TemplateView

from PIBD.models import Client, Contract, Proiect

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with transaction.atomic():
            proiecte = Proiect.objects.all()
            clienti = Client.objects.all()
        context['proiecte'] = proiecte
        context['clienti'] = clienti
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('addClient') is not None:

            client = Client()
            client.cnp = self.request.POST.get('CNP_add')
            client.nume = self.request.POST.get('NumeClient_add').upper()
            client.prenume = self.request.POST.get('Prenume_add')
            client.telefon = self.request.POST.get('Telefon_add')
            client.email = self.request.POST.get('Email_add')
            client.adresa = self.request.POST.get('Adresa_add')

            client.create()

        elif self.request.POST.get('addProiect') is not None:

            proiect = Proiect()
            proiect.nume = self.request.POST.get('Nume_add')
            proiect.status = self.request.POST.get('Status_add')
            proiect.tip = self.request.POST.get('Tip_add')
            proiect.start_date = parse(self.request.POST.get('Start_date_add'))
            proiect.finish_date = parse(self.request.POST.get('Finish_date_add'))
            proiect.create()

        elif self.request.POST.get('addContract') is not None:

            with transaction.atomic():
                client = Client.objects.get(id_client=int(self.request.POST.get('ID_Client_add')))
                proiect = Proiect.objects.get(id_proiect=int(self.request.POST.get('ID_Proiect_add')))

            contract = Contract()
            contract.client = client
            contract.proiect = proiect
            contract.team_name= self.request.POST.get('TEAM_NAME_add')
            contract.urgent = self.request.POST.get('Urgent_add')
            contract.deadline = self.request.POST.get('DEADLINE_add')
            contract.pret = self.request.POST.get('Pret_add')

            contract.create()

        return self.render_to_response(self.get_context_data())