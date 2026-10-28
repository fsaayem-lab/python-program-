# python-program-

def to_8bit(n):
    return format(n & 0xFF, '08b')


def signed_value(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


def add_binary(a, b):
    result = (a + b) & 0xFF
    binary = format(result, '08b')
    actual = a + b

    print("Operand 1:", a, "=", to_8bit(a))
    print("Operand 2:", b, "=", to_8bit(b))
    print("Binary result:", binary)
    print("Decimal result:", signed_value(binary))
    print("Actual sum:", actual)
    print("Overflow:", "Yes" if actual < -128 or actual > 127 else "No")
    print("-" * 30)


print("Expression (a): 120 + (+62)")
add_binary(120, 62)

print("Expression (b): (-120) + (-62)")
add_binary(-120, -62)
