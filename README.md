# FitId Library

FitId is a modular fitness tracking library that allows you to track workouts, nutrition, health metrics, and fitness goals. It also includes data visualization tools to help you analyze your fitness data.

## Project Structure

fitrack_library/ ├── fitrack/ │ ├── init.py │ ├── workout_tracker.py │ ├── nutrition_tracker.py │ ├── health_metrics.py │ ├── fitness_goals.py │ └── data_visualization.py └── README.md

## Installation

1. Clone or download the repository.
2. Ensure that the `fitrack` directory is in your Python path or install it as a package if needed.

## Usage

Here's an example of how to use the library:

```python
from fitrack.workout_tracker import WorkoutTracker
from fitrack.nutrition_tracker import NutritionTracker
from fitrack.health_metrics import HealthMetrics
from fitrack.fitness_goals import FitnessGoals
from fitrack.data_visualization import DataVisualization

# Create instances of the trackers
workout_tracker = WorkoutTracker()
nutrition_tracker = NutritionTracker()
health_metrics = HealthMetrics()
fitness_goals = FitnessGoals()

# Add a workout
workout_tracker.add_workout("Running", 30, 300)

# Add a meal
nutrition_tracker.add_meal("Grilled Chicken Salad", 350, {"proteins": 30, "fats": 10, "carbs": 20})

# Log weight data
health_metrics.log_weight(70, "2025-04-07")

# Set a fitness goal
fitness_goals.set_goal("weight_loss", 5)

# Create a data visualization instance
viz = DataVisualization(workout_tracker, nutrition_tracker, health_metrics, fitness_goals)
viz.generate_workout_chart()
