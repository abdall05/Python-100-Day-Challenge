PLACEHOLDER = "[name]"


def example_mail_reader(example_file_path):
    with open(example_file_path, 'r') as file:
        mail_content = file.read()
        return mail_content


def invited_names_extractor(invited_names_file_path):
    with open(invited_names_file_path, 'r') as file:
        invited_names = [line.strip() for line in file.readlines()]
    return invited_names


def mail_merge(example_file_path, invited_names_file_path, output_directory_path):
    example_mail_content = example_mail_reader(example_file_path)
    invited_names = invited_names_extractor(invited_names_file_path)
    for name in invited_names:
        generated_mail_path = f"{output_directory_path}/letter_for_{name}.txt"
        with open(generated_mail_path, 'w') as file:
            content = example_mail_content.replace(PLACEHOLDER, name)
            file.write(content)


example_path = 'Input/Letters/starting_letter.txt'
invited_names_path = 'Input/Names/invited_names.txt'
output_path = 'Output/ReadyToSend'
mail_merge(example_path, invited_names_path, output_path)
