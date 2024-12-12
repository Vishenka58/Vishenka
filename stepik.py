def decorator(func):
    def wrapper():
        return func().upper()

    return wrapper
@decorator
def imya():
    return input("Введите слово: ")
print("Привет, ", imya())
