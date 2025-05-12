import random

# DECORATOR 
def log_and_retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < n:
                print(f"Calling {func.__name__}... (Attempt {attempts + 1})")
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("Error:", e)
                    attempts += 1
            print("All attempts failed.")
        return wrapper
    return decorator

#  GENERATOR
def get_scores(students):
    for student in students:
        name = student["name"]
        for score in student["scores"]:
            yield name, score

# RECURSIVE AVERAGE
def average(scores):
    if not scores:
        return 0
    if len(scores) == 1:
        return scores[0]
    return (scores[0] + average(scores[1:]) * (len(scores) - 1)) / len(scores)

# FUNCTION TO APPLY DECORATOR 
@log_and_retry(3)
def generate_report(students):
    if random.choice([True, False]):  # Simulates a random failure
        raise Exception("Random failure during report generation.")
    
    print("\n Student Performance Report:")
    for student in students:
        avg = average(student["scores"])
        print(f"{student['name']} - Average Score: {avg:.2f}")

# MAIN
def main():
    students = [
        {"name": "Shalom", "scores": [70, 80,97,93,99, 90]},
        {"name": "Sophia", "scores": [60, 75, 88,90,85]},
    ]

    print(" Streaming Scores (via Generator):")
    for name, score in get_scores(students):
        print(f"{name} scored {score}")

    print("\n Generating Report (with Decorator + Retry):")
    generate_report(students)

main()
