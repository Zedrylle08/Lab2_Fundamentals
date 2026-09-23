import random
import string

# Student information
SURNAME = "Adonis"
SEED_NUM = 8

def generate_signal(surname, seed_num):
    random.seed(seed_num)

    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%*"

    extra_chars = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    signal = surname + str(seed_num) + "".join(extra_chars)
    return signal

def normalize_signal(signal):
    return signal.strip().upper()

def analyze_signal(signal):
    analysis = []
    for character in signal:
        if character.isalpha():
            category = "Letter"
        elif character.isdigit():
            category = "Number"
        elif character.isspace():
            category = "Space"
        else:
            category = "Special Character"

        analysis.append((character, category))
    return analysis

def classify_signal(signal):
    has_letter = any(c.isalpha() for c in signal)
    has_number = any(c.isdigit() for c in signal)

    if len(signal) >=8 and has_letter and has_number:
        return "VALID"
    else:
        return "INVALID"

generated_signal = generate_signal(SURNAME, SEED_NUM)
processed_signal = normalize_signal(generated_signal)
character_analysis = analyze_signal(processed_signal)
classification = classify_signal(processed_signal)

letter_count = sum(1 for c in str(processed_signal) if c.isalpha())
number_count = sum(1 for c in str(processed_signal) if c.isdigit())
space_count = sum(1 for c in str(processed_signal) if c.isspace())
special_count = sum(1 for c in str(processed_signal) if not c.isalnum() and not c.isspace())

print("==== TEXT SIGNAL DIAGNOSTIC REPORT ====")
print("Surname:", SURNAME)
print("SEED_NUM:", SEED_NUM)

print("\nGenerated Signal:", generated_signal)
print("Processed Signal:", processed_signal)

print("\nCharacter Analysis:")
for index, (character, category) in enumerate(character_analysis, start=1):
    print(f"{index}. {character} - {category}")

print("\nCharacter Summary:")
print("Letters:", letter_count)
print("Numbers:", number_count)
print("Spaces:", space_count)
print("Special Characters:", special_count)

print("\nSignal Classification:", classification)
print("Execution Log: All characters were analyzed.")
print("Final Output: Signal monitoring")