symvol = input("Type a symvol to find:")
text = input("Type a text to find a symvol:")

find = text.find(symvol)

if find == -1:
    print("Symvol doesn't exist in this text")
if find >= 0:
    print("Symvol exist in this text")
    print("The symvol in the text is the:", find+1)
