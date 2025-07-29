def sort(width, height, length, mass):
    # Calculate volume with formula provided
    volume = width * height * length

    # Is it bulky?
    is_bulky = (volume >= 1000000 or width >= 150 or height >= 150
                or length >= 150)

    # Is it heavy?
    is_heavy = mass >= 20

    # Classify
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


if __name__ == "__main__":
    assert sort(50, 50, 50, 10) == "STANDARD"
    assert sort(200, 50, 50, 10) == "SPECIAL"
    assert sort(50, 50, 50, 25) == "SPECIAL"
    assert sort(200, 200, 200, 30) == "REJECTED"
    assert sort(100, 100, 100, 19) == "SPECIAL"

    print("Tests successfully finalized.\n")

    packages = [
        (50, 50, 50, 10),
        (160, 40, 40, 15),
        (80, 90, 90, 25),
        (200, 200, 200, 30),
        (100, 100, 100, 19),
    ]

    print("Packages to sort by Thoughtful’s robot:\n")

    for index, (width, height, length, mass) in enumerate(packages, start=1):
        result = sort(width, height, length, mass)
        print(
            f"Package number {index}, with dimension {width}x{height}x{length} cm, and weight of {mass}kg -> Dispatched to -> {result} stack."
        )
