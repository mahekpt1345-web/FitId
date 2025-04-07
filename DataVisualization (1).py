import csv
from datetime import date as dt
from collections import defaultdict
import matplotlib.pyplot as plt

class DataVisualization:
    def __init__(self, workout_tracker, nutrition_tracker, health_metrics, fitness_goals):
        self.workout_tracker = workout_tracker
        self.nutrition_tracker = nutrition_tracker
        self.health_metrics = health_metrics
        self.fitness_goals = fitness_goals

    def generate_workout_chart(self):
        """Generate a line chart showing workout duration over time."""
        workouts = self.workout_tracker.view_workouts()
        if not workouts:
            print("No workout data available.")
            return
        dates = [w['date'] for w in workouts]
        durations = [w['duration'] for w in workouts]
        plt.figure()
        plt.plot(dates, durations, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Duration (min)')
        plt.title('Workout Duration Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def generate_calorie_chart(self):
        """Generate a bar chart of calories burned per workout."""
        workouts = self.workout_tracker.view_workouts()
        if not workouts:
            print("No workout data available.")
            return
        dates = [w['date'] for w in workouts]
        calories = [w['calories_burned'] for w in workouts]
        plt.figure()
        plt.bar(dates, calories)
        plt.xlabel('Date')
        plt.ylabel('Calories Burned')
        plt.title('Calories Burned Per Workout')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def generate_macronutrient_pie(self):
        """Generate a pie chart for macronutrient distribution."""
        macros = self.nutrition_tracker.track_macronutrients()
        labels = list(macros.keys())
        sizes = list(macros.values())
        plt.figure()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Macronutrient Distribution')
        plt.show()

    def generate_weight_trend_line(self):
        """Generate a line chart showing the weight trend over time."""
        weight_log = self.health_metrics.get_weight_trend()
        if not weight_log:
            print("No weight data available.")
            return
        dates = [entry['date'] for entry in weight_log]
        weights = [entry['weight'] for entry in weight_log]
        plt.figure()
        plt.plot(dates, weights, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Weight (kg)')
        plt.title('Weight Trend Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def compare_goal_progress(self, goal_type):
        """Generate a simple bar chart comparing progress vs. remaining for a goal."""
        goals = self.fitness_goals.view_all_goals()
        if goal_type not in goals:
            print("Goal type not found.")
            return
        goal = goals[goal_type]
        progress = goal['progress']
        remaining = goal['target'] - progress
        plt.figure()
        plt.bar(['Progress', 'Remaining'], [progress, remaining])
        plt.title(f'Goal Progress for {goal_type}')
        plt.show()

    def export_data_csv(self, data_type):
        """
        Export data to a CSV file.
        :param data_type: One of 'workout', 'nutrition', 'health', or 'goals'.
        """
        filename = f"{data_type}_data.csv"
        if data_type == 'workout':
            data = self.workout_tracker.view_workouts()
        elif data_type == 'nutrition':
            data = self.nutrition_tracker.view_daily_meals()
        elif data_type == 'health':
            data = self.health_metrics.weight_log
        elif data_type == 'goals':
            data = self.fitness_goals.view_all_goals()
        else:
            print("Invalid data type.")
            return
        if not data:
            print("No data available to export.")
            return
        keys = list(data[0].keys())
        with open(filename, 'w', newline='') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        print(f"Data exported to {filename}")

    def view_recent_stats(self):
        """Return a summary of the recent stats from various trackers."""
        summary = {
            'workouts': self.workout_tracker.get_workout_summary(),
            'nutrition': {
                'daily_calories': self.nutrition_tracker.calculate_daily_calories(),
                'macros': self.nutrition_tracker.track_macronutrients()
            },
            'health': self.health_metrics.get_recent_weight(),
            'goals': self.fitness_goals.view_all_goals()
        }
        return summary

    def visualize_heart_rate(self):
        """Generate a line chart for heart rate over time."""
        heart_rates = self.health_metrics.heart_rate_log
        if not heart_rates:
            print("No heart rate data available.")
            return
        times = [entry['time'] for entry in heart_rates]
        rates = [entry['heart_rate'] for entry in heart_rates]
        plt.figure()
        plt.plot(times, rates, marker='o')
        plt.xlabel('Time')
        plt.ylabel('Heart Rate')
        plt.title('Heart Rate Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def create_weekly_summary_chart(self):
        """Generate a bar chart summarizing weekly workout durations."""
        workouts = self.workout_tracker.view_workouts()
        if not workouts:
            print("No workout data available.")
            return
        summary = defaultdict(int)
        for workout in workouts:
            summary[workout['date']] += workout['duration']
        dates = list(summary.keys())
        durations = list(summary.values())
        plt.figure()
        plt.bar(dates, durations)
        plt.xlabel('Date')
        plt.ylabel('Total Duration (min)')
        plt.title('Weekly Workout Summary')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def reset_visualizations(self):
        """Reset any stored visualization state (if applicable)."""
        print("Visualizations reset.")

