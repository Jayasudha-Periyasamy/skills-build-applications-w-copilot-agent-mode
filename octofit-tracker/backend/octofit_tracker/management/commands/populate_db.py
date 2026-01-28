from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the database with test data for OctoFit Tracker'

    def handle(self, *args, **options):
        # Clear existing test data
        for obj in Leaderboard.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Activity.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Workout.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Team.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in User.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()

        # Create Users
        user1 = User.objects.create(username='alice', email='alice@example.com')
        user2 = User.objects.create(username='bob', email='bob@example.com')

        # Create Teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)
        team1.save()

        # Create Activities
        Activity.objects.create(user=user1, activity_type='run', duration=30, calories_burned=250, date='2023-01-01')
        Activity.objects.create(user=user2, activity_type='cycle', duration=45, calories_burned=400, date='2023-01-02')

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Strength')
        Workout.objects.create(name='Jogging', description='Jog for 15 minutes', suggested_for='Cardio')

        # Create Leaderboard
        Leaderboard.objects.create(team=team1, points=100)

        self.stdout.write(self.style.SUCCESS('Test data created successfully.'))
