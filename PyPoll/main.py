#open csv file
import os 
import csv

csvpath = os.path.join('.','PyPoll','election_data.csv')

with open (csvpath,newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    #header
    csv_header = next(csvreader)

    Totalnumbervotes = 0
    Candidateall = []
    for row in csvreader:
        if row[0] != None:
            Totalnumbervotes += 1
        if row[2] != None:
            Candidateall.append(row[2])

    Candidatename = []
    Candidate1 = 0
    Candidate2 = 0
    Candidate3 = 0
    Candidate4 = 0

    for i in range(len(Candidateall)-1):
        if Candidateall[i] not in Candidatename:
            Candidatename.append(Candidateall[i])
        if Candidateall[i] == Candidatename[0]:
            Candidate1 += 1
        elif Candidateall[i] == Candidatename[1]:
            Candidate2 += 1
        elif Candidateall[i] == Candidatename[2]:
            Candidate3 += 1
        elif Candidateall[i] == Candidatename[3]:
            Candidate4 += 1

    percentagevoteCandidate1 = round(Candidate1/Totalnumbervotes * 100, 4)
    percentagevoteCandidate2 = round(Candidate2/Totalnumbervotes * 100, 4)
    percentagevoteCandidate3 = round(Candidate3/Totalnumbervotes * 100, 4)
    percentagevoteCandidate4 = round(Candidate4/Totalnumbervotes * 100, 4)

    Candidate = {Candidatename[0]:Candidate1,Candidatename[1]:Candidate2,Candidatename[2]:Candidate3,Candidatename[3]:Candidate4}
    
    inverse = [(value, key) for key, value in Candidate.items()]
    winner = max(inverse)

    print(f''' Election Results 
            -------------------------
                Total Votes: {Totalnumbervotes}
            -------------------------
                {Candidatename[0]}: {percentagevoteCandidate1}% ({Candidate1})
                {Candidatename[1]}: {percentagevoteCandidate2}% ({Candidate2})
                {Candidatename[2]}: {percentagevoteCandidate3}% ({Candidate3})
                {Candidatename[3]}: {percentagevoteCandidate4}% ({Candidate4})
            -------------------------
                  Winner: {winner[1]}
            -------------------------''')

    with open(os.path.join('.','PyPoll','output.txt'), "w") as text_file:
        print(f''' Election Results 
            -------------------------
                Total Votes: {Totalnumbervotes}
            -------------------------
                {Candidatename[0]}: {percentagevoteCandidate1}% ({Candidate1})
                {Candidatename[1]}: {percentagevoteCandidate2}% ({Candidate2})
                {Candidatename[2]}: {percentagevoteCandidate3}% ({Candidate3})
                {Candidatename[3]}: {percentagevoteCandidate4}% ({Candidate4})
            -------------------------
                  Winner: {winner[1]}
            -------------------------''', file=text_file)
 


        
        