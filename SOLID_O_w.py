import io
import os

# The Output class is responsible for managing the output of data
# to different types of destinations.
class Output:
    def __init__(self, data, output_type):
        # output_type determines the destination type for the data.
        self.output_type = output_type
        self.data = data

    # The display method outputs the data to the chosen destination.
    def display(self):
        # If output_type is "console", the data is printed to the console.
        if self.output_type == "console":
            print(f"{self.data}")
        # If output_type is "file", the data is written to
        # a file in the script's directory.
        elif self.output_type == "file":
            # Get the directory that this script is in.
            file_dir = os.path.dirname(os.path.abspath(__file__))
            # Change the working directory to the directory of the script.
            os.chdir(file_dir)
            # Open the output file and write the data to it.
            with open('output.txt', 'w') as f:
                # Write the data to the file.
                f.write(self.data)
        # If output_type is neither "console" nor "file", raise an error.
        else:
            raise ValueError("Wrong type of output")

# Create an Output object with data "some string"
# and output_type "file", then call its display method.
obj = Output("some string","file")
obj.display()