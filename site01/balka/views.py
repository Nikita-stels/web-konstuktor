from django.shortcuts import render

def balka(request):
    return render(request, 'balka/balka.html')

def balkaras (request):
    dlina = int(request.POST['dlina'])
    nagruzka = int(request.POST['nagruzka'])

    max_moment = (nagruzka * dlina ** 2) / 8

    context = {
        'dlina' : dlina,
        'nagruzka' : nagruzka,
        'max_moment' : max_moment
    }

    return render(request, 'balka/balka01.html', context)