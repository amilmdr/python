reviewPos=["love","good", "great","nice","fine","cool"]
reviewNeg=["bad","worst", "not good","horrible","miserable"]

reviewU= input("Review:").lower()

if reviewU in reviewPos:
    print('positive')
elif reviewU in  reviewNeg:
    print('negative')
else:
    print("Neutral")