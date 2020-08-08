###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random

digits = list(range(10))
random.shuffle(digits)
randomNum = digits[:3]
print(randomNum)


def containsElement(l1, l2):
    for i in range(0, len(l1)):
        if l1[i] in l2:
            return True


def guessResult(num):
    nums = []
    while num != 0:
        num, remainder = divmod(num, 10)
        nums.append(remainder)
    nums.reverse()
    if nums == randomNum:
        return "CODE_CRACKED", -1
    for i in range(0, len(nums)):
        if nums[i] == randomNum[i]:
            return "Match", nums[i]
    if containsElement(randomNum, nums):
        return "Close", -1
    else:
        return "Nope", -1


# Another hint:
while True:
    guess = input("What is your guess? ")
    result, index = guessResult(int(guess))
    if index != -1:
        print("Match at {}".format(index))
    print("Result of your guess : {}".format(result))
    if result == "CODE_CRACKED":
        break

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
