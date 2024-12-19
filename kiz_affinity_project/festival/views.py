from rest_framework.decorators import api_view  
from rest_framework.response import Response 
from .models import Participant, DiscountCode  

@api_view(['POST'])  
def submit_quiz1(request):  
    data = request.data  
    name = data.get('name') 
    email = data.get('email')  
    score = data.get('score') 
    
    # Crée un enregistrement dans la base de données pour ce participant
    participant = Participant.objects.create(
        name=name,
        email=email,
        quiz_type="quiz1",  
        score=score
    )

    # Retourne une réponse JSON avec un message de succès
    return Response({"message": "Participant enregistré pour la tombola"})

@api_view(['POST'])  
def submit_quiz2(request):  
    data = request.data 
    name = data.get('name') 
    email = data.get('email') 
    score = data.get('score')  

    participant = Participant.objects.create(
        name=name,
        email=email,
        quiz_type="quiz2",  
        score=score
    )
    
    # Génère un code de réduction unique et l'associe au participant
    discount_code = DiscountCode.objects.create(participant=participant)

    # Retourne une réponse JSON avec un message de succès et le code généré
    return Response({"message": "Code de réduction généré", "code": discount_code.code})
