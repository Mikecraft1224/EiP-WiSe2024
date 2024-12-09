gifts = ['partridge in a pear tree', 'turtle doves', 'French hens', 'calling birds', 'gold rings','geese a-laying', \
'swans a-swimming', 'maids a-milking', 'ladies dancing', 'lords a-leaping', 'pipers piping', 'drummers drumming',]

# # Simple version
# for i in range(len(gifts)):
#     print("\nOn the", i+1, ". day of Christmas my true love sent to me:")

#     for j in range(0, i+1):
#         print(j+1, gifts[j])

# # Advanced version
# for i in range(len(gifts)):
#     print(f"\nOn the {i+1}. day of Christmas my true love sent to me:")

#     for j, gift in enumerate(gifts[:i+1]):
#         print(f"{j+1} {gift}")

for i in range(len(gifts)):
    print(f"\nOn the {i+1}. day of Christmas my true love sent to me:")
    # print("\nOn the", str(i+1) + ". day of Christmas my true love sent to me:")

    for j in range(i, -1, -1):
        if j == 0:
            print(f"And {j+1} {gifts[j]}")
            # print("And", j+1, gifts[j])
        else:
            print(f"{j+1} {gifts[j]}")
            # print(j+1, gifts[j])
