import random

win_pos = 100
player1_pos = 0
count = 0
player2_pos = 0

# Initial positions
print(f"Player1 is on the position {player1_pos}")
print(f"Player2 is on the position {player2_pos}")

def main(value, die, pos):
    match value:
        case 0:  # No play
            return pos, "no play"
        case 1:  # Ladder
            if pos + die <= win_pos:
                pos += die
            return pos, "ladder"
        case 2:  # Snake
            pos -= die
            if pos < 0:
                pos = 0
            return pos, "snake"
        case _:  # Default case to handle any unexpected value
            return pos, "no play"

# Game logic
while True:
    # Player 1 turn
    die = random.randint(1, 6)
    count += 1
    print("Player1 rolled:", die)

    value = random.randint(0, 2)
    player1_pos, event_name = main(value, die, player1_pos)

    print(f"Player1 event: {event_name}, position: {player1_pos}")

    if player1_pos == win_pos:
        print("Player1 wins the game!")
        print("Number of dice rolls to win:", count)
        break

    # Player 2 turn
    die = random.randint(1, 6)
    count += 1
    print("Player2 rolled:", die)

    value = random.randint(0, 2)
    player2_pos, event_name = main(value, die, player2_pos)

    print(f"Player2 event: {event_name}, position: {player2_pos}")

    if player2_pos == win_pos:
        print("Player2 wins the game!")
        print("Number of dice rolls to win:", count)
        break
