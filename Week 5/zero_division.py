
#Practige 1: ZeroDivisionError
# This code demonstrates how to handle a ZeroDivisionError exception.
# It prompts the user to enter the number of players and teams,
# then calculates the number of players per team.
# If the number of teams is zero, it raises a ZeroDivisionError.
# The exception is caught and a message is printed.
def main():
  try:
    players = int(input("Enter the number of players: "))
    teams = int(input("Enter the number of teams: "))
    players_per_team = players / teams
    print(f"Each team should have {players_per_team} players")
  except ZeroDivisionError as zero_div_err:
    print(zero_div_err)
if __name__ == "__main__":
  main()