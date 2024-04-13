N = input()
while True:
    for idx in range(len(N)-1):
        # find duplicates
        if N[idx] == N[idx+1]:
            # fix duplicate
            # Use the int() function to handle overflows and
            # set the remaining digits to all 0
            pair_index = idx + 2
            N = str(int(N[:pair_index])+1) + "0"*(len(N)-pair_index)

            # Restart the search for duplicates
            break
    else:
        # If the string has no duplicates, we are finished
        break

print(N)
