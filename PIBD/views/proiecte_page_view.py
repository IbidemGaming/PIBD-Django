from django.db import transaction
from django.views.generic import TemplateView
from dateutil.parser import parse

from PIBD.models import Proiect


class ProiectPageView(TemplateView):
    template_name = 'ListaProiecte.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with transaction.atomic():
            proiecte = Proiect.objects.all()
        context['proiecte'] = proiecte
        print(proiecte)

        return context


    def post(self, request, *args, **kwargs):
        if self.request.POST.get('updateProiect') is not None:

            proiect = Proiect.objects.get(id_proiect=int(self.request.POST.get('Select_proiect_Update')))

            nume = self.request.POST.get('Nume_update')
            nume = nume if nume != '' else proiect.nume

            status = self.request.POST.get('Status_update')
            status = status if status != '' else proiect.status

            tip = self.request.POST.get('Tip_update')
            tip = tip if tip != '' else proiect.tip

            start_date = self.request.POST.get('Start_date_update')
            start_date = parse(start_date) if start_date != '' else proiect.start_date

            finish_date = self.request.POST.get('Finish_date_update')
            finish_date = parse(finish_date) if finish_date != '' else proiect.finish_date

            proiect = Proiect(id_proiect=proiect.id_proiect, nume=nume,
                          status=status, tip=tip,
                          start_date=start_date, finish_date=finish_date)
            proiect.update()

        elif self.request.POST.get('deleteProiect') is not None:

            with transaction.atomic():
                proiect = Proiect.objects.get(id_proiect=int(self.request.POST.get('Select_proiect_Delete')))

            proiect.remove()

        return self.render_to_response(self.get_context_data())
