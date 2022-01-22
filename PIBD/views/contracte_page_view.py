from django.db import transaction
from django.views.generic import TemplateView
from dateutil.parser import parse

from PIBD.models import Contract


class ContractPageView(TemplateView):
    template_name = 'ListaContracte.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            contracte = Contract.objects.all()
        context['contracte'] = contracte
        return context

    def post(self, request, *args, **kwargs):

        if self.request.POST.get('updateContract') is not None:

            with transaction.atomic():
                contract = Contract.objects.get(id_contract=int(self.request.POST.get('Select_contract_Update')))

            client = contract.client
            proiect = contract.proiect

            team_name = self.request.POST.get('TEAM_NAME_update')
            team_name = team_name if team_name != '' else contract.team_name

            urgent = self.request.POST.get('URGENT_update')
            urgent = urgent if urgent != '' else contract.URGENT

            deadline = self.request.POST.get('DEADLINE_update')
            deadline = parse(deadline) if deadline != '' else contract.DEAD_LINE

            pret = self.request.POST.get('PRET_update')
            pret = pret if pret != '' else contract.pret

            contract = Contract(id_contract=contract.id_contract, client=client,
                                proiect=proiect, team_name=team_name,
                                urgent=urgent, deadline=deadline,
                                pret=pret)
            contract.update()

        elif self.request.POST.get('deleteContract') is not None:

            with transaction.atomic():
                contract = Contract.objects.get(
                    id_contract=int(self.request.POST.get('Select_contract_Delete')))

            contract.remove()

        return self.render_to_response(self.get_context_data())
