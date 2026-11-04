letters = "abcdefghij"
letters[0] == "a"
letters[2] == "c"
letters[-1] == "j"
letters[-2] == "i"

letters[1:3] == "bc"
letters[1:] == letters[1:len(letters)]
letters[:4] == letters[0:4] == "abcd"
letters[-3:-1] == "hi"

print(letters[0:len(letters):1])

print(letters[::-1])

demo = ["a", "b", "c"]
print(demo[::-1])

for i, letter in enumerate(demo):
    print(i, letter)