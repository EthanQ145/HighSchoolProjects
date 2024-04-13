socks = ['Red', 'Blue', 'Purple', 'Pink', 'Red', 'Blue', 'Purple', 'Pink']
found_sock = input()
for i in range(0, 6):
    if found_sock in socks:
        socks.remove(found_sock)
    found_sock = input()
if found_sock in socks:
    socks.remove(found_sock)
print(''.join(socks))
