"""
Visualized swimming script
by Aris Mandolini

26.06.2021
"""

demoText = "00:32,91 - 01:09,36 - 01:46,51 - 02:23,47 - 03:00,88 - 03:38,37 - 04:15,70 - 04:52,3605:29,78 - 06:07,71 - 06:45,36 - 07:23,32 - 08:01,17 - 08:40,22 - 09:18,32 - 09:55,6210:33,67 - 11  :10,50 - 11  :48,71 - 12:25,09 - 13:02,83 - 13:39,22 - 14:16,76 - 14:52,9815:29,59 - 16:05,66 - 16:40,28 - 17:16,53 - 17:52,20 - 18:23.87"

print("Input amount of athlets:")
numberOfAthlets = input()

numberOfAthlets = int(numberOfAthlets)

athleteMeta = []
athleteData = []

for currentAthleteNumber in range(numberOfAthlets):
    print("Please include name and other optional metadata for the athlete:")
    athleteMeta.append(input())
    print(f"Please include dataset for athlete number {currentAthleteNumber + 1} ({athleteMeta[currentAthleteNumber]}):")
    athleteData.append(input())
    print(athleteMeta[currentAthleteNumber])
    print(athleteData[currentAthleteNumber])
