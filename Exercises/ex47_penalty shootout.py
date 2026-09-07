# 47. Penalty Shootout
# Simulate a football penalty shootout with sudden death rules.
import time
import random


def penalty_shootout():
    striker_choices = ["Left", "Middle", "Right"]
    goalkeeper_choices = ["Left", "Middle", "Right"]

    score_A, score_B = 0, 0
    shots_taken = 0
    attempt = 1  # Represents the current pair of kicks (e.g., attempt 1 for A and B)
    current_team = 0  # 0 for Team A, 1 for Team B
    game_over = False

    print("--- Penalty Shootout ---")

    # Initial 5 kicks per team
    while shots_taken < 10 and not game_over:
        if current_team == 0:
            print(f"\nAttempt {attempt}")
            team_label = "Team A"
        else:
            team_label = "Team B"

        print(f"{team_label}'s turn")

        # Striker's choice
        shoot = input(f"{team_label} Striker, choose your position (Left, Middle, Right): ").strip().capitalize()
        while shoot not in striker_choices:
            print("Invalid choice. Please choose from Left, Middle, Right.")
            shoot = input(f"{team_label} Striker, choose your position (Left, Middle, Right): ").strip().capitalize()

        # Goalkeeper's random choice
        keeper = random.choice(goalkeeper_choices)

        print(f"The striker shoots to the {shoot.upper()}")
        time.sleep(1)  # Reduced sleep for faster simulation
        print(f"The goalkeeper dives to the {keeper.upper()}")
        time.sleep(1)  # Reduced sleep for faster simulation

        # Determine goal or miss: Goal if striker direction != goalkeeper direction
        if shoot != keeper:
            print("GOAL!!")
            if current_team == 0:
                score_A += 1
            else:
                score_B += 1
        else:
            print("MISSED!!")

        shots_taken += 1

        # Check for Early Finish Rule (only if enough shots have been taken to make a difference)
        if 2 <= shots_taken < 10:
            # Calculate max possible score for each team given remaining shots
            # remaining for A = 5 - (shots A has taken)
            # remaining for B = 5 - (shots B has taken)
            shots_A_taken = (shots_taken + (1 if current_team == 1 else 0)) // 2
            shots_B_taken = (shots_taken + (1 if current_team == 0 else 0)) // 2

            max_possible_score_A = score_A + (5 - shots_A_taken)
            max_possible_score_B = score_B + (5 - shots_B_taken)

            if score_A > max_possible_score_B:  # Team A leads and B cannot catch up
                print(f"\nEarly finish! {team_label} wins with an unassailable lead.")
                game_over = True
            elif score_B > max_possible_score_A:  # Team B leads and A cannot catch up
                print(f"\nEarly finish! {team_label} wins with an unassailable lead.")
                game_over = True

        # Switch teams for the next shot
        current_team = 1 - current_team  # Toggles between 0 and 1

        # # If it's Team A's turn next, it means an attempt is complete,
        # and not all initial 10 shots are done
        if current_team == 0 and shots_taken < 10:
            attempt += 1

        print(f"Current Score: Team A: {score_A} - Team B: {score_B}")

    # Sudden Death
    if not game_over and score_A == score_B:
        print("\n--- Sudden Death Round ---")
        sudden_death_round = 1
        while not game_over:
            print(f"\nSudden Death Round {sudden_death_round}")

            # Team A's turn
            print("Team A's turn")
            shoot_A = input("Team A Striker, choose your position (Left, Middle, Right): ").strip().capitalize()
            while shoot_A not in striker_choices:
                print("Invalid choice. Please choose from Left, Middle, Right.")
                shoot_A = input("Team A Striker, choose your position (Left, Middle, Right): ").strip().capitalize()
            keeper_A = random.choice(goalkeeper_choices)
            print(f"Team A striker shoots to the {shoot_A.upper()}")
            time.sleep(1)
            print(f"Team A goalkeeper dives to the {keeper_A.upper()}")
            time.sleep(1)

            team_A_scored = (shoot_A != keeper_A)
            if team_A_scored:
                print("Team A GOAL!!")
                score_A += 1
            else:
                print("Team A MISSED!!")

            print(f"Current Score: Team A: {score_A} - Team B: {score_B}")

            # Team B's turn
            print("\nTeam B's turn")
            shoot_B = input("Team B Striker, choose your position (Left, Middle, Right): ").strip().capitalize()
            while shoot_B not in striker_choices:
                print("Invalid choice. Please choose from Left, Middle, Right.")
                shoot_B = input("Team B Striker, choose your position (Left, Middle, Right): ").strip().capitalize()
            keeper_B = random.choice(goalkeeper_choices)
            print(f"Team B striker shoots to the {shoot_B.upper()}")
            time.sleep(1)
            print(f"Team B goalkeeper dives to the {keeper_B.upper()}")
            time.sleep(1)

            team_B_scored = (shoot_B != keeper_B)
            if team_B_scored:
                print("Team B GOAL!!")
                score_B += 1
            else:
                print("Team B MISSED!!")

            print(f"Current Score: Team A: {score_A} - Team B: {score_B}")

            # Check for sudden death winner
            if team_A_scored and not team_B_scored:
                print("\nTeam A wins in Sudden Death!")
                game_over = True
            elif not team_A_scored and team_B_scored:
                print("\nTeam B wins in Sudden Death!")
                game_over = True

            sudden_death_round += 1

    # Display the final result
    print("\n=====================================")
    print("Final Result:")
    print(f"Team A {score_A} - {score_B} Team B")
    if score_A > score_B:
        print("Team A wins!!")
    elif score_A < score_B:
        print("Team B wins!!")
    else:
        print("It's a draw (should not happen if sudden death is implemented correctly)!")
    print("=====================================")


# Call the function to play the game
penalty_shootout()
