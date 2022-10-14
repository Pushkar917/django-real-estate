from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from apps.profiles.models import Profile
from apps.profiles.exceptions import  ProfileNotFound
from .models import Rating

User = get_user_model()

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    print("----------------------")
    print(profile_id)
    try:
        profile_agent = Profile.objects.get(id=profile_id, is_agent=True)
    except Profile.DoesNotExist:
        raise ProfileNotFound
        
    data = request.data
    user = User.objects.get(pkid=profile_agent.user.pkid)
    if user.email == request.user.email:
        formatted_response = {"message": "You can't rate yourself"}
        return Response(formatted_response, status = status.HTTP_403_FORBIDDEN)

    alreadyExists = profile_agent.agent_review.filter(agent__pkid = user.pkid).exists()
    
    if alreadyExists:
        formatted_response = {"detail": "Profile already reviewed"}
        return Response(formatted_response, status=status.HTTP_403_FORBIDDEN)
    elif data['rating'] == 0:
        formatted_response = {"detail": "Please select a rating"}
        return Response(formatted_response, status=status.HTTP_403_FORBIDDEN)
    else:
        review = Rating.objects.create(
            rater= request.user,
            agent = profile_agent,
            rating = data['rating'],
            comment = data['comment']
        )

        reviews = profile_agent.agent_review.all()
        profile_agent.num_reviews = len(reviews)
        total = 0
        for i in reviews:
            total += i.rating

        return Response("Review Added")


