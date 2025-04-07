import csv
from datetime import date as dt
from collections import defaultdict
import matplotlib.pyplot as plt
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
