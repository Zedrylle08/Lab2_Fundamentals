import random

# Student informations
SURNAME = "Adonis"
SEED_NUM = 8

# Generate unique sensor data surname and seed
seed_value = sum(ord(char) for char in SURNAME) + SEED_NUM
random.seed(seed_value)

sensor_data = [random.randint(0, 100) for _ in range(5)]
print("=== SENSOR MONITORING SYSTEM ===")
print(f"Surname: {SURNAME}")
print(f"SEED_NUM: {SEED_NUM}")
print(f"Generated Sensor Data: {sensor_data}")

# Operating ranges
def classify(reading):
    if reading < 0 or reading > 100:
        return "INVALID"
    elif reading <= 30:
        return "LOW"
    elif reading <= 60:
        return "NORMAL"
    else:
        return "HIGH"

valid_results = []
invalid_results = []
classifications = []

print("\n===PROCESSING READINGS ===")

for i, reading in enumerate(sensor_data, start=1):
    try:
        value = float(reading)

        if value < 0 or value > 100:
            invalid_results.append(reading)
            print(f"Reading {i}:{reading} -> INVALID")
        else:
            category = classify(value)
            valid_results.append(reading)
            classifications.append(category)
            print(f"Reading{i}:{reading} -> {category}")
    except ValueError:
        invalid_results.append(reading)
        print(f"Reading{i}:{reading} -> INVALID")

print("\n=== SUMMARY ===")
print(f"Valid/Invalid Results: {len(valid_results)} valid, {len(invalid_results)} invalid")
print(f"Classification Results: {classifications}")
print("Execution Log: All generated readings were validated and classified.")

print("\n=== FINAL OUTPUT ===")
print("Sensor monitoring completed successfully.")
