users = {
    "admin": "1234",
    "user": "abcd"
}

percobaan = 0

while percobaan < 3:
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Logi gagal!")
        percobaan +=1 

if percobaan == 3:
    print("Akun diblokir!")