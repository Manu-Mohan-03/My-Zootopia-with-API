"""Creates a html page about animals """
import data_fetcher


def get_animal_info(animal_data):
    """ Gets the only required information about animals from the JSON CONTENT
    fox_data: List of dictionaries which contains data from JSON file
    skin_type: The skin type filter chosen by user
    return: String containing the required data for the browser
    """
    animal_info_str = ""
    # adding information to a string
    for animal in animal_data:
        # For Serialization
        animal_info_str += serialize_animal(animal)

    return animal_info_str


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
    html_template = html_template.replace("__REPLACE_ANIMALS_INFO__",
                                          new_string)
    return html_template

def write_file(file_path, contents):
    """To open the file for writing"""
    with open(file_path, "w", encoding = "utf-8") as handle:
        handle.write(contents)


def error_html(unknown_phrase):
    """To display missing information page"""
    html_body = f"<h2>The animal '{unknown_phrase}' doesn't exist.</h2>"
    return html_body


def main():
    animal = input("Enter name of an animal: ")
    try:
        animals_data = data_fetcher.fetch_data(animal)
    except Exception as error:
        print(error)
        return None
    if animals_data:
        animals_info = get_animal_info(animals_data)
        animals_html = edit_html_template("animals_template.html",animals_info)
    else:
        animals_html = error_html(animal)
    write_file("animals.html", animals_html)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()