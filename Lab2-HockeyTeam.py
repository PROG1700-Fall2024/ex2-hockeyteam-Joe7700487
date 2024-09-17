# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations

def main():
    #define variables
    team = input("Name a team: ")
    wins = int(input("How many wins do they have?  "))
    losses = int(input("How many losses do they have? "))

    #calculate win percent and convert to string to append % sign
    ratio = str('%.2f' % ((wins / losses) * 100)) + "%!"

    #print final answer
    print(team, "has", wins, "wins and", losses, "losses with a win ratio of", ratio)
main()