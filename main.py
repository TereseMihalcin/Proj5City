import matplotlib.pyplot as plt
import numpy as np
import random

# Project 5
# Terese Mihalcin and Germaine Uwimpuhwe

people = 150
x = [random.randint(1, 200) for i in range(people)]
y = [random.randint(1, 200) for i in range(people)]

peoplePoints = np.zeros((len(x), 2))
for i in range(len(x)):
    peoplePoints[i] = (x[i])
    peoplePoints[i, 1] = (y[i])

hotels = 20
a = [random.randint(1, 200) for i in range(hotels)]
b = [random.randint(1, 200) for i in range(hotels)]

hotelPoints = np.zeros((len(a), 2))
for i in range(len(a)):
    hotelPoints[i] = (a[i])
    hotelPoints[i, 1] = (b[i])

fig, ax = plt.subplots()
plt.grid(True)
plt.scatter(x, y)
plt.scatter(a, b)
# changed range to 20 for testing purposes should be (0,200)
plt.xlim(0, 200)
plt.ylim(0, 200)

# allows the scale to increment by 1
ax.yaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_major_locator(plt.MultipleLocator(1))

# show plot
plt.show()


# find euclidean distance function
def euclidean_distance(coordinate1, coordinate2):
    return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2), .5)


distances = []

guestsHotel_0 = []
guestsHotel_1 = []
guestsHotel_2 = []
guestsHotel_3 = []
guestsHotel_4 = []
guestsHotel_5 = []
guestsHotel_6 = []
guestsHotel_7 = []
guestsHotel_8 = []
guestsHotel_9 = []
guestsHotel_10 = []
guestsHotel_11 = []
guestsHotel_12 = []
guestsHotel_13 = []
guestsHotel_14 = []
guestsHotel_15 = []
guestsHotel_16 = []
guestsHotel_17 = []
guestsHotel_18 = []
guestsHotel_19 = []

CountHotel_0 = 0
CountHotel_1 = 0
CountHotel_2 = 0
CountHotel_3 = 0
CountHotel_4 = 0
CountHotel_5 = 0
CountHotel_6 = 0
CountHotel_7 = 0
CountHotel_8 = 0
CountHotel_9 = 0
CountHotel_10 = 0
CountHotel_11 = 0
CountHotel_12 = 0
CountHotel_13 = 0
CountHotel_14 = 0
CountHotel_15 = 0
CountHotel_16 = 0
CountHotel_17 = 0
CountHotel_18 = 0
CountHotel_19 = 0

# finds the distance between each individual person to each hotel
for i in range(len(x)):
    for j in range(len(a)):
        distances += [euclidean_distance(peoplePoints[i], hotelPoints[j])]

    # distance to the closest hotel to each person
    closestHotelDistance = min(distances[i * 20:(i + 1) * 20])

    # each persons distance from each hotel
    personDistance = distances[i * 20:(i + 1) * 20]

    # the hotel number closest to each person
    closestHotelNum = personDistance.index(closestHotelDistance)

    if closestHotelNum == 0:
        CountHotel_0 = CountHotel_0 + 1
        guestsHotel_0 += [i]
        if CountHotel_0 == 15:
            print("Hotel 0 is full")
            hotelPoints[0] = 5000
    elif closestHotelNum == 1:
        CountHotel_1 = CountHotel_1 + 1
        guestsHotel_1 += [i]
        if CountHotel_1 == 15:
            print("Hotel 1 is full")
            hotelPoints[1] = 5000
    elif closestHotelNum == 2:
        CountHotel_2 = CountHotel_2 + 1
        guestsHotel_2 += [i]
        if CountHotel_2 == 15:
            print("Hotel 2 is full")
            hotelPoints[2] = 5000
    elif closestHotelNum == 3:
        CountHotel_3 = CountHotel_3 + 1
        guestsHotel_3 += [i]
        if CountHotel_3 == 15:
            print("Hotel 3 is full")
            hotelPoints[3] = 5000
    elif closestHotelNum == 4:
        CountHotel_4 = CountHotel_4 + 1
        guestsHotel_4 += [i]
        if CountHotel_4 == 15:
            print("Hotel 4 is full")
            hotelPoints[4] = 5000
    elif closestHotelNum == 5:
        CountHotel_5 = CountHotel_5 + 1
        guestsHotel_5 += [i]
        if CountHotel_5 == 15:
            print("Hotel 5 is full")
            hotelPoints[5] = 5000
    elif closestHotelNum == 6:
        CountHotel_6 = CountHotel_6 + 1
        guestsHotel_6 += [i]
        if CountHotel_6 == 15:
            print("Hotel 6 is full")
            hotelPoints[6] = 5000
    elif closestHotelNum == 7:
        CountHotel_7 = CountHotel_7 + 1
        guestsHotel_7 += [i]
        if CountHotel_7 == 15:
            print("Hotel 7 is full")
            hotelPoints[7] = 5000
    elif closestHotelNum == 8:
        CountHotel_8 = CountHotel_8 + 1
        guestsHotel_8 += [i]
        if CountHotel_8 == 15:
            print("Hotel 8 is full")
            hotelPoints[8] = 5000
    elif closestHotelNum == 9:
        CountHotel_9 = CountHotel_9 + 1
        guestsHotel_9 += [i]
        if CountHotel_9 == 15:
            print("Hotel 9 is full")
            hotelPoints[9] = 5000
    elif closestHotelNum == 10:
        CountHotel_10 = CountHotel_10 + 1
        guestsHotel_10 += [i]
        if CountHotel_10 == 15:
            print("Hotel 10 is full")
            hotelPoints[10] = 5000
    elif closestHotelNum == 11:
        CountHotel_11 = CountHotel_11 + 1
        guestsHotel_11 += [i]
        if CountHotel_11 == 15:
            print("Hotel 11 is full")
            hotelPoints[11] = 5000
    elif closestHotelNum == 12:
        CountHotel_12 = CountHotel_12 + 1
        guestsHotel_12 += [i]
        if CountHotel_12 == 15:
            print("Hotel 12 is full")
            hotelPoints[12] = 5000
    elif closestHotelNum == 13:
        CountHotel_13 = CountHotel_13 + 1
        guestsHotel_13 += [i]
        if CountHotel_13 == 15:
            print("Hotel 13 is full")
            hotelPoints[13] = 5000
    elif closestHotelNum == 14:
        CountHotel_14 = CountHotel_14 + 1
        guestsHotel_14 += [i]
        if CountHotel_14 == 15:
            print("Hotel 14 is full")
            hotelPoints[14] = 5000
    elif closestHotelNum == 15:
        CountHotel_15 = CountHotel_15 + 1
        guestsHotel_15 += [i]
        if CountHotel_15 == 15:
            print("Hotel 15 is full")
            hotelPoints[15] = 5000
    elif closestHotelNum == 16:
        CountHotel_16 = CountHotel_16 + 1
        guestsHotel_16 += [i]
        if CountHotel_16 == 15:
            print("Hotel 16 is full")
            hotelPoints[16] = 5000
    elif closestHotelNum == 17:
        CountHotel_17 = CountHotel_17 + 1
        guestsHotel_17 += [i]
        if CountHotel_17 == 15:
            print("Hotel 17 is full")
            hotelPoints[17] = 5000
    elif closestHotelNum == 18:
        CountHotel_18 = CountHotel_18 + 1
        guestsHotel_18 += [i]
        if CountHotel_18 == 15:
            print("Hotel 18 is full")
            hotelPoints[18] = 5000
    elif closestHotelNum == 19:
        CountHotel_19 = CountHotel_19 + 1
        guestsHotel_19 += [i]
        if CountHotel_19 == 15:
            print("Hotel 19 is full")
            hotelPoints[19] = 5000

print("Occupancy for each hotel is:", CountHotel_0, CountHotel_1, CountHotel_2, CountHotel_3, CountHotel_4, CountHotel_5, CountHotel_6, CountHotel_7, CountHotel_8, CountHotel_9, CountHotel_10, CountHotel_11, CountHotel_12, CountHotel_13, CountHotel_14, CountHotel_15, CountHotel_16, CountHotel_17, CountHotel_18, CountHotel_19)

print("total amount of people in hotels:", CountHotel_0+CountHotel_1+CountHotel_2+CountHotel_3+CountHotel_4+CountHotel_5+CountHotel_6+CountHotel_7+CountHotel_8+CountHotel_9+CountHotel_10+CountHotel_11+CountHotel_12+CountHotel_13+CountHotel_14+CountHotel_15+CountHotel_16+CountHotel_17+CountHotel_18+CountHotel_19)

print("Hotel 0's guests include:", guestsHotel_0)
print("Hotel 1's guests include:", guestsHotel_1)
print("Hotel 2's guests include:", guestsHotel_2)
print("Hotel 3's guests include:", guestsHotel_3)
print("Hotel 4's guests include:", guestsHotel_4)
print("Hotel 5's guests include:", guestsHotel_5)
print("Hotel 6's guests include:", guestsHotel_6)
print("Hotel 7's guests include:", guestsHotel_7)
print("Hotel 8's guests include:", guestsHotel_8)
print("Hotel 9's guests include:", guestsHotel_9)
print("Hotel 10's guests include:", guestsHotel_10)
print("Hotel 11's guests include:", guestsHotel_11)
print("Hotel 12's guests include:", guestsHotel_12)
print("Hotel 13's guests include:", guestsHotel_13)
print("Hotel 14's guests include:", guestsHotel_14)
print("Hotel 15's guests include:", guestsHotel_15)
print("Hotel 16's guests include:", guestsHotel_16)
print("Hotel 17's guests include:", guestsHotel_17)
print("Hotel 18's guests include:", guestsHotel_18)
print("Hotel 19's guests include:", guestsHotel_19)
