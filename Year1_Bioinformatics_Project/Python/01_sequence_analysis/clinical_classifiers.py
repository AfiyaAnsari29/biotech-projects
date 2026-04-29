#1
systolic= int(input("Enter systolic blood pressure:")) # Get systolic value from user
diastolic= int(input("Enter diastolic blood pressure:")) # Get diastolic value from user

# Classification based on standard blood pressure ranges

if systolic<120 and diastolic<80:
    classification="Normal"
elif 120<=systolic<=129 and diastolic<80:
    classification="Elevated"
elif (130<=systolic<=139) or (80<=diastolic<=89):
    classification="Hypertension Stage 1"
elif systolic>=140 or diastolic>=90:
    classification="Hypertension Stage 2"
else:
    classification="Undefined/ mixed category"

print(f"Classification:{classification}")


#2
dna="ATCGATTGAGCTCTAGC"  # Example DNA sequence
counts={"A":0, "T":0, "C":0, "G":0} # Initialize counts dictionary

# Loop through each base and increment its count

for base in dna:
    if base in counts:
        counts[base] +=1

print("DNA Base Counts:", counts)

