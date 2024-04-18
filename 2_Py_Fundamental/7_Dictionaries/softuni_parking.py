data_base = {}

n = int(input())

for _ in range(n):

    entry_line = input().split()

    validation_status = entry_line[0]

    if len(entry_line) == 3 and validation_status == 'register':
        username = entry_line[1]
        license_plate = entry_line[2]
        if username in data_base.keys():
            curr_license_plate = data_base[username]
            print(f"ERROR: already registered with plate number {curr_license_plate}")
        else:
            print(f"{username} registered {license_plate} successfully")
        data_base[username] = license_plate
    elif len(entry_line) == 2 and validation_status == 'unregister':
        username = entry_line[1]
        if username not in data_base.keys():
            print(f"ERROR: user {username} not found")
        else:
            data_base.pop(username)
            print(f"{username} unregistered successfully")

for curr_users, curr_plate_numbers in data_base.items():
    print(f"{curr_users} => {curr_plate_numbers}")
