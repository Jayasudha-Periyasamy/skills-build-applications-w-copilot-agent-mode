# Script to populate MongoDB with test data for OctoFit Tracker
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

def run():
    # Create Users
    user1 = User.objects.create(username='alice', email='alice@example.com')
    user2 = User.objects.create(username='bob', email='bob@example.com')

    # Create Teams
    team1 = Team.objects.create(name='Team Alpha')
    team1.members.add(user1, user2)

    # Create Activities
    Activity.objects.create(user=user1, activity_type='run', duration=30, calories_burned=250, date='2023-01-01')
    Activity.objects.create(user=user2, activity_type='cycle', duration=45, calories_burned=400, date='2023-01-02')

    # Create Workouts
    Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Strength')
    Workout.objects.create(name='Jogging', description='Jog for 15 minutes', suggested_for='Cardio')

    # Create Leaderboard
    Leaderboard.objects.create(team=team1, points=100)

if __name__ == "__main__":
    run()
