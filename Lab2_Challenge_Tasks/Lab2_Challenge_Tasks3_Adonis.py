# Student information
SURNAME = "Adonis"
SEED_NUM = 8

# 1. Generate the password and attempt limit
def generate_credentials(surname, seed_num):
    password = surname.upper() + str(seed_num)
    attempt_limit = seed_num
    return password, attempt_limit


# 2. Normalize the password entered by the user
def normalize_password(password):
    return password.strip().upper()


# 3. Manage the authentication process
def authenticate(correct_password, attempt_limit):
    attempts_made = 0
    access_granted = False
    execution_log = []

    while attempts_made < attempt_limit:
        entered_password = input("Enter password: ")
        processed_password = normalize_password(entered_password)

        attempts_made += 1

        if processed_password == correct_password:
            access_granted = True
            execution_log.append(
                f"Attempt {attempts_made}: Access granted."
            )
            break
        else:
            execution_log.append(
                f"Attempt {attempts_made}: Incorrect password."
            )
            remaining = attempt_limit - attempts_made

            if remaining > 0:
                print("Incorrect password. Attempts remaining:", remaining)

    # 4. Determine the final system state
    if access_granted:
        access_result = "ACCESS GRANTED"
        final_system_state = "UNLOCKED"
    else:
        access_result = "ACCESS DENIED"
        final_system_state = "LOCKED"

    return attempts_made, access_result, final_system_state, execution_log


# 5. Run the system
generated_password, attempt_limit = generate_credentials(
    SURNAME, SEED_NUM
)

print("===== PASSWORD AUTHENTICATION REPORT =====")
print("Surname:", SURNAME)
print("SEED_NUM:", SEED_NUM)

print("\nGenerated Password:", generated_password)
print("Attempt Limit:", attempt_limit)

attempts_made, access_result, final_system_state, execution_log = authenticate(
    generated_password, attempt_limit
)

# 6. Display the assessment report
print("\n===== ASSESSMENT DATA =====")
print("Generated Password:", generated_password)
print("Attempt Limit:", attempt_limit)
print("Attempts Made:", attempts_made)
print("Access Result:", access_result)
print("Final System State:", final_system_state)

print("\nExecution Log:")
for log in execution_log:
    print(log)

print("\nFinal Output: Authentication process completed.")