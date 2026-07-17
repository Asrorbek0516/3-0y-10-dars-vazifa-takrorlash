def greet(ism, til="uz"):
    if til == "uz":
        return f"Salom, {ism}!"
    elif til == "en":
        return f"Hello, {ism}!"
    elif til == "ru":
        return f"Привет, {ism}!"
    else:
        return f"Til qollab-quvvatlanmaydi, {ism}!"

print(greet("Ali", 'ru'))