from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PieceUtiliseeFormSet, InterventionForm, PieceUtiliseeForm
from .utils import lire_fichier_excel
from .models import OrderWork, Intervention, PieceUtilisee
from django.utils import timezone

# Create your views here.
@login_required
def home_main(request):
    chemin_fichier = "C:/Users/kfoke/Desktop/BASE_ARRET.xlsx"
    donnees = lire_fichier_excel(chemin_fichier=chemin_fichier)
    colonnes = ['CODE']
    donnees_filtre = donnees[colonnes]
    interventions = OrderWork.objects.filter(executant=request.user)
    interventions_dict = {intervention.code: intervention for intervention in interventions}
    return render(request, 'maintenance/home_main.html', {'donnees': donnees_filtre, 'interventions_dict': interventions_dict})

@login_required
def home_pro(request):
    return render(request, 'production/home_pro.html')

@login_required
def home_admin(request):
    return render(request, 'base_admin.html')

@login_required
def enregistrer_heure_debut(request, code):
    if request.method == 'POST':
        orderwork, created = OrderWork.objects.get_or_create(
            executant=request.user, 
            code=code,
            )
        if not orderwork.heure_debut:
            orderwork.heure_debut = timezone.now()
            orderwork.save()
            return JsonResponse({'status': 'ok', 'heure_debut': orderwork.heure_debut})
        else:
            return JsonResponse({'status': 'existe', 'heure_debut': orderwork.heure_debut})

@login_required
def enregistrer_heure_fin(request, code):
    if request.method == 'POST':
        orderwork = get_object_or_404(OrderWork, executant=request.user, code=code)
        if not orderwork.heure_fin:
            orderwork.heure_fin = timezone.now()
            orderwork.save()
            return JsonResponse({'status': 'ok', 'heure_fin': orderwork.heure_fin})
        else:
            return JsonResponse({'status': 'existe', 'heure_fin': orderwork.heure_fin})

@login_required
def verifier_heures(request, code):
    try:
        orderwork = OrderWork.objects.get(code=code)
        heure_debut = orderwork.heure_debut.isoformat() if orderwork.heure_debut else None
        heure_fin = orderwork.heure_fin.isoformat() if orderwork.heure_fin else None
        first_user = orderwork.executant.username if orderwork.heure_debut else None
        return JsonResponse({'heure_debut': heure_debut, 'heure_fin': heure_fin, 'first_user': first_user})
    except OrderWork.DoesNotExist:
        return JsonResponse({'heure_debut': None, 'heure_fin': None, 'first_user': None})

def runwork(request, code):
    return render(request, 'maintenance/start_work.html', {'code': code})

@login_required
def tache_effectue(request):
    orderword = OrderWork.objects.filter(executant=request.user, heure_fin__isnull=False)
    return render(request, 'maintenance/tache_effectue.html', {'orderwork': orderword})

@login_required
def faire_rapport(request, code):
    code = code.split()[-1]
    print(f"Code nettoyé: {code}")
    try: 
        orderwork = OrderWork.objects.get(code=code)
        print(f"OrderWork trouvé: {orderwork}")
    except OrderWork.DoesNotExist: 
        print(f"OrderWork avec le code {code} n'existe pas.")

    intervention, created  = Intervention.objects.get_or_create(ordre_travail=orderwork, utilisateur=request.user, defaults={'classe_action': 'AUTOMATISME'})
    print(f"Intervention trouvée: {intervention}")
    print(f"Intervention trouvée ou créée: {intervention} (créée: {created})")
    if request.method == 'POST':
        form = InterventionForm(request.POST, instance=intervention)
        piece_formset = PieceUtiliseeFormSet(request.POST, prefix='pieces')
        if form.is_valid() and piece_formset.is_valid():
            # Sauvegarder l'intervention sans la lier aux pièces pour le moment
            intervention = form.save(commit=False) 
            intervention.utilisateur = request.user 
            intervention.ordre_travail = orderwork
            intervention.save()

            pieces = piece_formset.save(commit=False)
            for piece in pieces:
                piece.intervention = intervention
                piece.ordre_travail = orderwork
                piece.save()
            return redirect('tache_effectue')
    else:
        form = InterventionForm(instance=intervention)
        piece_formset = PieceUtiliseeFormSet(prefix='pieces')
    return render(request, 'maintenance/faire_rapport.html', {'form': form, 'piece_formset': piece_formset, 'orderwork': orderwork})

@login_required
def ajouter_piece_utilisee(request, code): 
    orderwork = get_object_or_404(OrderWork, code=code)
    piece_formset = PieceUtiliseeFormSet(prefix='pieces') 
    return render(request, 'maintenance/piece_utilisee.html', {'piece_formset': piece_formset, 'orderwork': orderwork})