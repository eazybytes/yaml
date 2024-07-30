import yaml
import os

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def display_data(data):
    for key, value in data.items():
        print(f"{key}:")
        print(value)

def main(file_path):
    data = read_yaml(file_path)
    display_data(data)

if __name__ == "__main__":
    # Assuming the YAML file is in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file_path = os.path.join(script_dir, 'long_strings.yml')
    main(yaml_file_path)
