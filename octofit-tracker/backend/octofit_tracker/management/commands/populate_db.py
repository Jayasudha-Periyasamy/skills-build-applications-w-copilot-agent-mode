from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the database with test data for OctoFit Tracker'

    def handle(self, *args, **options):
        # Create Users
        user1, _ = User.objects.get_or_create(username='alice', email='alice@example.com')
        user2, _ = User.objects.get_or_create(username='bob', email='bob@example.com')

        # Create Teams
        team1, _ = Team.objects.get_or_create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Create Activities
        Activity.objects.get_or_create(user=user1, activity_type='run', duration=30, calories_burned=250, date='2023-01-01')
        Activity.objects.get_or_create(user=user2, activity_type='cycle', duration=45, calories_burned=400, date='2023-01-02')

        # Create Workouts
        Workout.objects.get_or_create(name='Pushups', description='Do 20 pushups', suggested_for='Strength')
        Workout.objects.get_or_create(name='Jogging', description='Jog for 15 minutes', suggested_for='Cardio')

        # Create Leaderboard
        Leaderboard.objects.get_or_create(team=team1, points=100)

        self.stdout.write(self.style.SUCCESS('Test data created successfully.'))
