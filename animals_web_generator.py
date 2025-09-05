import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_info(fox_data, skin_type):
    """ Gets the only required information about animals from the JSON CONTENT
    fox_data: List of dictionaries which contains data from JSON file
    skin_type: The skin type filter chosen by user
    return: String containing the required data for the browser
    """
    animal_info_str = ""
    # adding information to a string
    for fox in fox_data:
        # Display all contents if user choose *
        if skin_type is None:
            # For Serialization
            animal_info_str += serialize_animal(fox)
        elif skin_type == fox.get("characteristics").get("skin_type").lower():
            # For Serialization
            animal_info_str += serialize_animal(fox)

    return animal_info_str


def get_skin_types(fox_data):
    """To show the different skin types for the user to chose"""
    skin_types = set()
    for fox in fox_data:
        skin_type = fox.get("characteristics").get("skin_type")
        skin_types.add(skin_type.lower())
    return skin_types

def serialize_animal(animal_obj):
    """To populate the html contents needed to display the required details"""
    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<div class="card__text">\n'
    output += '<ul>\n'
    if animal_obj.get("characteristics").get("diet"):
        output += f'<li><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n'
    if animal_obj.get("locations") and len(animal_obj.get("locations")) > 0:
        output += f'<li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'
    if animal_obj.get("characteristics").get("type"):
        output += f'<li><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'
    if animal_obj.get("characteristics").get("skin_type"):
        output += (f'<li><strong>Skin Type:</strong> '
                   f'{animal_obj["characteristics"]["skin_type"]}</li>\n')
    output += '</ul>\n'
    output += '</div>\n'
    output += '</li>\n'
    return output


def edit_html_template(file_path,new_string):
    """Open the html file for reading"""
    with open(file_path,"r", encoding="utf-8") as handle:
        html_template = handle.read()
    html_template = html_template.replace("__REPLACE_ANIMALS_INFO__", new_string)
    return html_template

def write_file(file_path, contents):
    """To open the file for writing"""
    with open(file_path, "w", encoding = "utf-8") as handle:
        handle.write(contents)


def user_prompt(skin_types):
    """ Selection screen for the user(* to skip the filter)"""
    while True:
        input_str = f"Please select a skin type from {skin_types} or '*' to ignore skin selection: "
        skin_type = input(input_str)
        if skin_type.lower() in skin_types:
            return skin_type.lower()
        elif skin_type == '*':
            return None


def main():
    animals_data = load_data('animals_data.json')
    skin_types_set = get_skin_types(animals_data)
    skin_type = user_prompt(skin_types_set)
    animals_info = get_animal_info(animals_data, skin_type)
    animals_html = edit_html_template("animals_template.html",animals_info)
    write_file("animals.html", animals_html)


if __name__ == "__main__":
    main()