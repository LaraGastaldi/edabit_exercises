def relation_to_luke(name):
    dici = {"Dart Vader": "father", "Leia": "sister", "Han": "brother in law", "R2D2": "droid"}
    if dici[name]:
        return "Luke, I am your "+dici[name]

print(relation_to_luke("Dart Vader"))