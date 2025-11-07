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


class NutritionTracker:
    def __init__(self):
        self.meals = []
        self.next_id = 1
        self.daily_calorie_goal = 0

    def add_meal(self, meal_name, calories, macros):
        """
        Add a meal.
        :param meal_name: Name/description of the meal.
        :param calories: Calories in the meal.
        :param macros: Dictionary with macronutrient info (e.g., proteins, fats, carbs).
        :return: The meal dictionary.
        """
        meal = {
            'id': self.next_id,
            'meal_name': meal_name,
            'calories': calories,
            'macros': macros
        }
        self.meals.append(meal)
        self.next_id += 1
        return meal

    def remove_meal(self, meal_id):
        """Remove a meal by its id."""
        self.meals = [m for m in self.meals if m['id'] != meal_id]

    def view_daily_meals(self):
        """Return all meals logged for the day."""
        return self.meals

    def calculate_daily_calories(self):
        """Return the sum of calories consumed."""
        return sum(m['calories'] for m in self.meals)

    def track_macronutrients(self):
        """Aggregate macronutrients for the day."""
        total_macros = {'proteins': 0, 'fats': 0, 'carbs': 0}
        for meal in self.meals:
            total_macros['proteins'] += meal['macros'].get('proteins', 0)
            total_macros['fats'] += meal['macros'].get('fats', 0)
            total_macros['carbs'] += meal['macros'].get('carbs', 0)
        return total_macros

    def suggest_meal(self, target_calories):
        """Suggest a meal based on target calories (dummy implementation)."""
        suggestions = [
            {'meal_name': 'Grilled Chicken Salad', 'calories': 350},
            {'meal_name': 'Veggie Wrap', 'calories': 300},
            {'meal_name': 'Protein Smoothie', 'calories': 250}
        ]
        suggestions.sort(key=lambda x: abs(x['calories'] - target_calories))
        return suggestions[0]

    def set_daily_calorie_goal(self, calorie_goal):
        """Set the daily calorie goal."""
        self.daily_calorie_goal = calorie_goal

    def get_remaining_calories(self):
        """Return remaining calories for the day."""
        consumed = self.calculate_daily_calories()
        return self.daily_calorie_goal - consumed

    def generate_grocery_list(self, meal_plan):
        """
        Generate a grocery list from a meal plan.
        :param meal_plan: List of meal names.
        :return: List of grocery items.
        """
        grocery_items = {
            'Grilled Chicken Salad': ['chicken breast', 'lettuce', 'tomatoes', 'cucumber'],
            'Veggie Wrap': ['tortilla', 'spinach', 'bell peppers', 'hummus'],
            'Protein Smoothie': ['protein powder', 'banana', 'almond milk']
        }
        grocery_list = set()
        for meal in meal_plan:
            items = grocery_items.get(meal, [])
            grocery_list.update(items)
        return list(grocery_list)

    def reset_tracker(self):
        """Clear all nutrition data."""
        self.meals = []
        self.next_id = 1


class HealthMetrics:
    def __init__(self):
        self.weight_log = []  # List of dicts: {weight, date}
        self.height_log = []  # List of dicts: {height, date}
        self.heart_rate_log = []  # List of dicts: {heart_rate, time}

    def calculate_bmi(self, weight, height):
        """
        Calculate Body Mass Index.
        :param weight: Weight in kilograms.
        :param height: Height in meters.
        :return: BMI value.
        """
        if height <= 0:
            return None
        return weight / (height ** 2)

    def calculate_body_fat_percentage(self, age, gender, bmi):
        """
        Calculate body fat percentage using a dummy formula.
        :param age: Age in years.
        :param gender: 'male' or 'female'.
        :param bmi: Calculated BMI.
        :return: Body fat percentage.
        """
        if gender.lower() == 'male':
            body_fat = 1.20 * bmi + 0.23 * age - 16.2
        else:
            body_fat = 1.20 * bmi + 0.23 * age - 5.4
        return body_fat

    def log_weight(self, weight, date):
        """Log weight data."""
        self.weight_log.append({'weight': weight, 'date': date})

    def log_height(self, height, date):
        """Log height data."""
        self.height_log.append({'height': height, 'date': date})

    def get_recent_weight(self):
        """Return the most recent weight entry."""
        if self.weight_log:
            return self.weight_log[-1]
        return None

    def get_weight_trend(self):
        """Return the weight log (trend over time)."""
        return self.weight_log

    def suggest_ideal_weight(self, height, age, gender):
        """
        Suggest an ideal weight.
        Here, ideal weight is calculated for a BMI of 22.
        """
        ideal_bmi = 22
        ideal_weight = ideal_bmi * (height ** 2)
        return ideal_weight

    def log_heart_rate(self, heart_rate, time):
        """Log heart rate data."""
        self.heart_rate_log.append({'heart_rate': heart_rate, 'time': time})

    def get_average_heart_rate(self, duration=None):
        """
        Calculate the average heart rate.
        The duration parameter can be used to filter data in a real application.
        """
        if not self.heart_rate_log:
            return None
        total = sum(entry['heart_rate'] for entry in self.heart_rate_log)
        return total / len(self.heart_rate_log)

    def reset_metrics(self):
        """Clear all health metrics data."""
        self.weight_log = []
        self.height_log = []
        self.heart_rate_log = []


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


class DataVisualization:
    def __init__(self, workout_tracker: WorkoutTracker, nutrition_tracker: NutritionTracker, 
                 health_metrics: HealthMetrics, fitness_goals: FitnessGoals):
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
