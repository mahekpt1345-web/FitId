import csv
from datetime import date as dt
from collections import defaultdict
import matplotlib.pyplot as plt
class FitnessGoals:
    def __init__(self):
        self.goals = {}

    def set_goal(self, goal_type, target):
        """
        Set a new fitness goal.
        :param goal_type: The type of goal (e.g., 'weight_loss').
        :param target: The target value to reach.
        """
        self.goals[goal_type] = {'target': target, 'progress': 0, 'deadline': None}

    def get_goal_progress(self):
        """Return the progress for each goal."""
        return {k: v['progress'] for k, v in self.goals.items()}

    def update_goal_progress(self, goal_type, progress):
        """Update the progress for a specific goal."""
        if goal_type in self.goals:
            self.goals[goal_type]['progress'] += progress

    def get_remaining_goal(self, goal_type):
        """Return the remaining amount to reach the goal."""
        if goal_type in self.goals:
            goal = self.goals[goal_type]
            return goal['target'] - goal['progress']
        return None

    def suggest_steps_to_goal(self, goal_type):
        """
        Suggest daily steps to reach the goal by dividing the remaining amount over 30 days.
        """
        remaining = self.get_remaining_goal(goal_type)
        if remaining is None:
            return None
        return remaining / 30

    def generate_progress_report(self):
        """Generate a report summarizing the progress for all goals."""
        report = {}
        for goal_type, goal in self.goals.items():
            report[goal_type] = {
                'target': goal['target'],
                'progress': goal['progress'],
                'remaining': goal['target'] - goal['progress'],
                'deadline': goal['deadline']
            }
        return report

    def set_deadline(self, goal_type, deadline):
        """Set a deadline for a specific goal."""
        if goal_type in self.goals:
            self.goals[goal_type]['deadline'] = deadline

    def adjust_goal(self, goal_type, new_target):
        """Adjust the target of an existing goal."""
        if goal_type in self.goals:
            self.goals[goal_type]['target'] = new_target

    def view_all_goals(self):
        """Return all goals with details."""
        return self.goals

    def reset_all_goals(self):
        """Clear all fitness goals."""
        self.goals = {}
