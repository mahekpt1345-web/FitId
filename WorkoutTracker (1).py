import csv
from datetime import date as dt
from collections import defaultdict
import matplotlib.pyplot as plt
class WorkoutTracker:
    def __init__(self):
        self.workouts = []
        self.next_id = 1

    def add_workout(self, name, duration, calories_burned, date=None):
        """
        Add a workout entry.
        :param name: Name/description of the workout.
        :param duration: Duration in minutes.
        :param calories_burned: Calories burned.
        :param date: (Optional) Date string; defaults to today's date.
        :return: The workout dictionary.
        """
        if date is None:
            date = dt.today().isoformat()
        workout = {
            'id': self.next_id,
            'name': name,
            'duration': duration,
            'calories_burned': calories_burned,
            'date': date
        }
        self.workouts.append(workout)
        self.next_id += 1
        return workout

    def remove_workout(self, workout_id):
        """Remove a workout by its id."""
        self.workouts = [w for w in self.workouts if w['id'] != workout_id]

    def view_workouts(self):
        """Return all logged workouts."""
        return self.workouts

    def calculate_total_duration(self):
        """Return the total duration of all workouts."""
        return sum(w['duration'] for w in self.workouts)

    def calculate_total_calories(self):
        """Return the total calories burned."""
        return sum(w['calories_burned'] for w in self.workouts)

    def get_workout_by_date(self, search_date):
        """Return workouts logged on a specific date."""
        return [w for w in self.workouts if w['date'] == search_date]

    def suggest_workout(self, goal_type):
        """Suggest a workout based on the given goal type."""
        suggestions = {
            'cardio': 'Running',
            'strength': 'Weight lifting',
            'flexibility': 'Yoga'
        }
        return suggestions.get(goal_type.lower(), 'General Fitness')

    def generate_weekly_plan(self, goal_type):
        """Generate a dummy weekly workout plan based on a goal type."""
        plan = []
        suggestion = self.suggest_workout(goal_type)
        for day in range(7):
            plan.append({'day': day + 1, 'workout': suggestion})
        return plan

    def get_workout_summary(self):
        """Return a summary of workouts."""
        summary = {
            'total_workouts': len(self.workouts),
            'total_duration': self.calculate_total_duration(),
            'total_calories': self.calculate_total_calories()
        }
        return summary

    def reset_tracker(self):
        """Clear all workout data."""
        self.workouts = []
        self.next_id = 1
