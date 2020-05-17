from django.shortcuts import render, get_object_or_404
from .models import Cursit


def paginait(request):
    its = Cursit.objects.order_by('-date')
    return render(request, 'paginait.html', {'its': its})


def postari(request, pkit_id):
    postare = get_object_or_404(Cursit, pk=pkit_id)

    return render(request, 'postari.html', {'postare': postare})
