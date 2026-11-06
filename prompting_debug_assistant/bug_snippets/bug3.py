users = {
    "aydan": "aydan@example.com",
    "murad": "murad@example.com"
}


def find_user_email(username):
    email = users.get(username)
    return email.lower()


def main():
    username = "samir"
    result = find_user_email(username)

    if result:
        print(f"Email: {result}")
    else:
        print("User not found")


if __name__ == "__main__":
    main()
