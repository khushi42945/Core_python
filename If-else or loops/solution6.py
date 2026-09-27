def user_slug(text):
    text = text.lower()
    result= []

    for char in text:
        if char.isalnum():
            result.append(char)
        else:
            if result and result[-1] != "-":
                result.append("-")

    return "".join(result).strip("-")


user_title = input("Enter article title: ")

slug = user_slug(user_title)

print("Generated Slug", slug)