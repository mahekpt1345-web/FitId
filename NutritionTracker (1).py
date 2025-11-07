import csv
from datetime import date as dt
from collections import defaultdict
import matplotlib.pyplot as plt

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
