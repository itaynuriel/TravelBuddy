from .models import User,UserPreferences,PersonalityProfile, Trip

def get_user_data(user_id):
    user = User.query.get(user_id)
    personality_profile = PersonalityProfile.query.filter_by(user_id=user_id).first()
    user_preferences = UserPreferences.query.filter_by(user_id=user_id).first()
    
    return user, personality_profile, user_preferences

def get_users_in_same_cluster(cluster):
    users = User.query.filter_by(cluster=cluster).all()
    return users





