import yaml
import pprint


def read_yaml():
    """ A function to read YAML file"""
    with open('/home/girish/catkin_ws/location_recorder.yaml') as f:
        config = yaml.safe_load(f)

    return config


if __name__ == "__main__":
    # read the config yaml
    my_config = read_yaml()

    print(my_config)