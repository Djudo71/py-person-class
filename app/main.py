class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_dicts: list[dict]) -> list[Person]:
    Person.people = {}

    person_instances = [Person(p["name"], p["age"]) for p in people_dicts]

    for person_dict in people_dicts:
        current_person_name = person_dict["name"]
        current_person_obj = Person.people[current_person_name]

        wife_name = person_dict.get("wife")
        if wife_name:
            if wife_name in Person.people:
                current_person_obj.wife = Person.people[wife_name]
            else:
                print(f"Warning: Wife \"{wife_name}\" not found for "
                      f"\"{current_person_obj.name}\".")

        husband_name = person_dict.get("husband")
        if husband_name:
            if husband_name in Person.people:
                current_person_obj.husband = Person.people[husband_name]
            else:
                print(f"Warning: Husband \"{husband_name}\" not found for "
                      f"\"{current_person_obj.name}\".")

    return person_instances
