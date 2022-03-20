import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

print("Welcome to the annual selection of the new principle.\nAs per the tradition, only 6 candidates will be nominated.\nPlease proceed to input candidate's names.")
print("-------------------")

# Using list comprehension to iterate over an input 6 times and append the name of participants in candidates_names
candidates_names =[input("Name of the candidate: ") for number in range(6)]
### For further readability ^^^^  
# candidates_names = []
# for number in range(6):
#     added_candidates_names = input("Name of the candidate: ")
#     candidates_names.append(added_candidates_names)

print("-------------------")
#Each variable takes int as input relating to their index in candidates_names list
#####This requires an update to achive usability and less redudancy####
candidate_1 = int(input(f"How many voters for {candidates_names[0]}: "))
candidate_2 = int(input(f"How many voters for {candidates_names[1]}: "))
candidate_3 = int(input(f"How many voters for {candidates_names[2]}: "))
candidate_4 = int(input(f"How many voters for {candidates_names[3]}: "))
candidate_5 = int(input(f"How many voters for {candidates_names[4]}: "))
candidate_6 = int(input(f"How many voters for {candidates_names[5]}: "))

#Appends candidate variables into voter (number of votes) list.
voters = []
voters.extend((candidate_1,candidate_2,candidate_3,candidate_4,candidate_5,candidate_6))

#So far we have two lists, one for candidates names and other for number of votes
#Converting two lists into a dictionary with two keys and each has its own key-value assigned
dictionary_candidates_voters = {'candidates': candidates_names, 'voters': voters}

print("-------------------")
#Converting a dictionary into a DataFrame using Pandas and indexing them starting with 1 instead of 0
df_candidates_voters = pd.DataFrame(dictionary_candidates_voters, index =[1,2,3,4,5,6])
#Beautifying tabel using tabulate module assigning keys of dictionary as main headers 
print(tabulate(df_candidates_voters, headers='keys', tablefmt='fancy_grid'))
print("-------------------")
print("The new principple for 2021/2022 is..")
#Subsetting the highest number of votes in a candidate using max() method
subset= df_candidates_voters[df_candidates_voters.voters == df_candidates_voters.voters.max()]
print(tabulate(subset, headers='keys', tablefmt='fancy_grid'))

#Using matplotlib to showcase results of the votes in bar presentation 
plt.bar(candidates_names, voters, color = "maroon")
plt.title("Results for the new principle of the leauge 2021/2022")
plt.xlabel("Number of Votes")
plt.ylabel("Candidates Names")
plt.show()
