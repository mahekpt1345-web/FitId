# example_usage.py

from FitTrack import WorkoutTracker, NutritionTracker, HealthMetrics, FitnessGoals, DataVisualization

def workout_menu(workout_tracker):
    while True:
        print("\n--- Workout Tracker Menu ---")
        print("1. Add Workout")
        print("2. Remove Workout")
        print("3. View Workouts")
        print("4. Calculate Total Duration")
        print("5. Calculate Total Calories")
        print("6. Get Workout by Date")
        print("7. Suggest Workout")
        print("8. Generate Weekly Plan")
        print("9. Get Workout Summary")
        print("10. Reset Tracker")
        print("11. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == "1":
            name = input("Enter workout name: ")
            duration = float(input("Enter duration in minutes: "))
            calories = float(input("Enter calories burned: "))
            date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
            workout = workout_tracker.add_workout(name, duration, calories, date_str if date_str else None)
            print("Workout added:", workout)
        elif choice == "2":
            workout_id = int(input("Enter workout id to remove: "))
            workout_tracker.remove_workout(workout_id)
            print("Workout removed.")
        elif choice == "3":
            print("Workouts:", workout_tracker.view_workouts())
        elif choice == "4":
            print("Total Duration:", workout_tracker.calculate_total_duration())
        elif choice == "5":
            print("Total Calories Burned:", workout_tracker.calculate_total_calories())
        elif choice == "6":
            date_str = input("Enter date (YYYY-MM-DD): ")
            print("Workouts on", date_str, ":", workout_tracker.get_workout_by_date(date_str))
        elif choice == "7":
            goal_type = input("Enter goal type (cardio, strength, flexibility): ")
            print("Workout suggestion:", workout_tracker.suggest_workout(goal_type))
        elif choice == "8":
            goal_type = input("Enter goal type for weekly plan: ")
            print("Weekly Plan:", workout_tracker.generate_weekly_plan(goal_type))
        elif choice == "9":
            print("Workout Summary:", workout_tracker.get_workout_summary())
        elif choice == "10":
            workout_tracker.reset_tracker()
            print("Workout tracker reset.")
        elif choice == "11":
            break
        else:
            print("Invalid choice. Please try again.")

def nutrition_menu(nutrition_tracker):
    while True:
        print("\n--- Nutrition Tracker Menu ---")
        print("1. Add Meal")
        print("2. Remove Meal")
        print("3. View Daily Meals")
        print("4. Calculate Daily Calories")
        print("5. Track Macronutrients")
        print("6. Suggest Meal")
        print("7. Set Daily Calorie Goal")
        print("8. Get Remaining Calories")
        print("9. Generate Grocery List")
        print("10. Reset Tracker")
        print("11. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == "1":
            meal_name = input("Enter meal name: ")
            calories = float(input("Enter calories: "))
            proteins = float(input("Enter proteins (g): "))
            fats = float(input("Enter fats (g): "))
            carbs = float(input("Enter carbs (g): "))
            macros = {"proteins": proteins, "fats": fats, "carbs": carbs}
            meal = nutrition_tracker.add_meal(meal_name, calories, macros)
            print("Meal added:", meal)
        elif choice == "2":
            meal_id = int(input("Enter meal id to remove: "))
            nutrition_tracker.remove_meal(meal_id)
            print("Meal removed.")
        elif choice == "3":
            print("Daily Meals:", nutrition_tracker.view_daily_meals())
        elif choice == "4":
            print("Daily Calorie Consumption:", nutrition_tracker.calculate_daily_calories())
        elif choice == "5":
            print("Macronutrient Totals:", nutrition_tracker.track_macronutrients())
        elif choice == "6":
            target_calories = float(input("Enter target calories: "))
            print("Meal suggestion:", nutrition_tracker.suggest_meal(target_calories))
        elif choice == "7":
            calorie_goal = float(input("Enter daily calorie goal: "))
            nutrition_tracker.set_daily_calorie_goal(calorie_goal)
            print("Daily calorie goal set.")
        elif choice == "8":
            print("Remaining Calories:", nutrition_tracker.get_remaining_calories())
        elif choice == "9":
            meal_plan_str = input("Enter meal plan as comma-separated meal names: ")
            meal_plan = [m.strip() for m in meal_plan_str.split(",")]
            grocery_list = nutrition_tracker.generate_grocery_list(meal_plan)
            print("Grocery List:", grocery_list)
        elif choice == "10":
            nutrition_tracker.reset_tracker()
            print("Nutrition tracker reset.")
        elif choice == "11":
            break
        else:
            print("Invalid choice. Please try again.")

def health_menu(health_metrics):
    while True:
        print("\n--- Health Metrics Menu ---")
        print("1. Calculate BMI")
        print("2. Calculate Body Fat Percentage")
        print("3. Log Weight")
        print("4. Log Height")
        print("5. Get Recent Weight")
        print("6. Get Weight Trend")
        print("7. Suggest Ideal Weight")
        print("8. Log Heart Rate")
        print("9. Get Average Heart Rate")
        print("10. Reset Metrics")
        print("11. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == "1":
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            bmi = health_metrics.calculate_bmi(weight, height)
            print("BMI:", bmi)
        elif choice == "2":
            age = int(input("Enter age: "))
            gender = input("Enter gender (male/female): ")
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            bmi = health_metrics.calculate_bmi(weight, height)
            body_fat = health_metrics.calculate_body_fat_percentage(age, gender, bmi)
            print("Body Fat Percentage:", body_fat)
        elif choice == "3":
            weight = float(input("Enter weight (kg): "))
            date_str = input("Enter date (YYYY-MM-DD): ")
            health_metrics.log_weight(weight, date_str)
            print("Weight logged.")
        elif choice == "4":
            height = float(input("Enter height (m): "))
            date_str = input("Enter date (YYYY-MM-DD): ")
            health_metrics.log_height(height, date_str)
            print("Height logged.")
        elif choice == "5":
            print("Recent Weight:", health_metrics.get_recent_weight())
        elif choice == "6":
            print("Weight Trend:", health_metrics.get_weight_trend())
        elif choice == "7":
            height = float(input("Enter height (m): "))
            age = int(input("Enter age: "))
            gender = input("Enter gender (male/female): ")
            ideal_weight = health_metrics.suggest_ideal_weight(height, age, gender)
            print("Suggested Ideal Weight:", ideal_weight)
        elif choice == "8":
            heart_rate = float(input("Enter heart rate: "))
            time_str = input("Enter time (HH:MM): ")
            health_metrics.log_heart_rate(heart_rate, time_str)
            print("Heart rate logged.")
        elif choice == "9":
            print("Average Heart Rate:", health_metrics.get_average_heart_rate())
        elif choice == "10":
            health_metrics.reset_metrics()
            print("Health metrics reset.")
        elif choice == "11":
            break
        else:
            print("Invalid choice. Please try again.")

def fitness_menu(fitness_goals):
    while True:
        print("\n--- Fitness Goals Menu ---")
        print("1. Set Goal")
        print("2. Get Goal Progress")
        print("3. Update Goal Progress")
        print("4. Get Remaining Goal")
        print("5. Suggest Steps to Goal")
        print("6. Generate Progress Report")
        print("7. Set Deadline")
        print("8. Adjust Goal")
        print("9. View All Goals")
        print("10. Reset All Goals")
        print("11. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == "1":
            goal_type = input("Enter goal type: ")
            target = float(input("Enter target: "))
            fitness_goals.set_goal(goal_type, target)
            print("Goal set.")
        elif choice == "2":
            print("Goal Progress:", fitness_goals.get_goal_progress())
        elif choice == "3":
            goal_type = input("Enter goal type: ")
            progress = float(input("Enter progress to add: "))
            fitness_goals.update_goal_progress(goal_type, progress)
            print("Goal progress updated.")
        elif choice == "4":
            goal_type = input("Enter goal type: ")
            print("Remaining for", goal_type, ":", fitness_goals.get_remaining_goal(goal_type))
        elif choice == "5":
            goal_type = input("Enter goal type: ")
            print("Suggested Steps per Day:", fitness_goals.suggest_steps_to_goal(goal_type))
        elif choice == "6":
            print("Progress Report:", fitness_goals.generate_progress_report())
        elif choice == "7":
            goal_type = input("Enter goal type: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            fitness_goals.set_deadline(goal_type, deadline)
            print("Deadline set.")
        elif choice == "8":
            goal_type = input("Enter goal type: ")
            new_target = float(input("Enter new target: "))
            fitness_goals.adjust_goal(goal_type, new_target)
            print("Goal adjusted.")
        elif choice == "9":
            print("All Goals:", fitness_goals.view_all_goals())
        elif choice == "10":
            fitness_goals.reset_all_goals()
            print("All goals reset.")
        elif choice == "11":
            break
        else:
            print("Invalid choice. Please try again.")

def data_visualization_menu(data_viz):
    while True:
        print("\n--- Data Visualization Menu ---")
        print("1. Generate Workout Chart")
        print("2. Generate Calorie Chart")
        print("3. Generate Macronutrient Pie")
        print("4. Generate Weight Trend Line")
        print("5. Compare Goal Progress")
        print("6. Export Data CSV")
        print("7. View Recent Stats")
        print("8. Visualize Heart Rate")
        print("9. Create Weekly Summary Chart")
        print("10. Reset Visualizations")
        print("11. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == "1":
            data_viz.generate_workout_chart()
        elif choice == "2":
            data_viz.generate_calorie_chart()
        elif choice == "3":
            data_viz.generate_macronutrient_pie()
        elif choice == "4":
            data_viz.generate_weight_trend_line()
        elif choice == "5":
            goal_type = input("Enter goal type to compare: ")
            data_viz.compare_goal_progress(goal_type)
        elif choice == "6":
            print("Data types available: workout, nutrition, health, goals")
            data_type = input("Enter data type: ")
            data_viz.export_data_csv(data_type)
        elif choice == "7":
            print("Recent Stats:", data_viz.view_recent_stats())
        elif choice == "8":
            data_viz.visualize_heart_rate()
        elif choice == "9":
            data_viz.create_weekly_summary_chart()
        elif choice == "10":
            data_viz.reset_visualizations()
        elif choice == "11":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    # Initialize all trackers and the visualization class.
    workout_tracker = WorkoutTracker()
    nutrition_tracker = NutritionTracker()
    health_metrics = HealthMetrics()
    fitness_goals = FitnessGoals()
    data_viz = DataVisualization(workout_tracker, nutrition_tracker, health_metrics, fitness_goals)

    while True:
        print("\n=== FitTrack Main Menu ===")
        print("1. Workout Tracker")
        print("2. Nutrition Tracker")
        print("3. Health Metrics")
        print("4. Fitness Goals")
        print("5. Data Visualization")
        print("6. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            workout_menu(workout_tracker)
        elif choice == "2":
            nutrition_menu(nutrition_tracker)
        elif choice == "3":
            health_menu(health_metrics)
        elif choice == "4":
            fitness_menu(fitness_goals)
        elif choice == "5":
            data_visualization_menu(data_viz)
        elif choice == "6":
            print("Exiting FitTrack. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
