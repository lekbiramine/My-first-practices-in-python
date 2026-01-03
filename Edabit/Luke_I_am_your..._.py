def relation_to_luke(name: str) -> str:
    """Return Luke's relation to the given character."""
    family = {
        "Darth Vader":"father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid"
    }
    return f"Luke, I am your {family.get(name)}."
print(relation_to_luke("Darth Vader"))