import wordcloud  # Used to generate word clouds from text
import matplotlib.pyplot as plt  # Used to display the generated word cloud
import os  # For file path operations
import pathlib  # To handle paths in a cross-platform way

# Custom exception class to handle file not found errors
class FileNotFoundError(Exception):
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return f"file {self.filename} doesn't exist."


# Custom exception class to handle invalid input data
class InvalidInputDataError(Exception):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"invalid input data error: {self.content}"

# Custom exception class to handle disk space full error scenarios
class DiskSpaceFullError(Exception):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"DiskSpaceFullError: {self.content}"

# Function to process the given text file, compute word/character frequencies, and generate a word cloud
def Processing_text_file(filename):
    with open(filename, 'r') as file:
        content = file.read().lower()  # Read and convert content to lowercase
        
        # Check if content is a valid string
        if not isinstance(content, str):
            raise InvalidInputDataError("Expected String but got non-string value.")
        if not content.strip():
            raise InvalidInputDataError("Input data is missing or empty.")

        # Remove special characters from content
        special = ',."\''  
        for i in special:
            content = content.replace(i, '')


        # Calculate word frequencies
        words = content.split()

        # Check for disk space limit (50 words)
        if len(words) > 10:
            raise DiskSpaceFullError("Input contains more than 10 words. Disk space full.")
        
        word_dic = {}
        for word in words:
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1

        # Calculate character frequencies
        char_dic = {}
        for char in content:
            if char in char_dic:
                char_dic[char] += 1
            else:
                char_dic[char] = 1

        # Generate the word cloud from the content
        file_wc = wordcloud.WordCloud()
        file_wc.generate(content)
    
    return word_dic, char_dic, file_wc

# Function to display the generated word cloud and save it as an image
def showCloud(wc, filename='wordcloud.png'):
    wc.to_file(filename)  # Save the word cloud to a file
    plt.imshow(wc, interpolation='bilinear')  # Display the word cloud
    plt.axis('off')  # Hide the axes
    plt.show()  # Render the plot

# Function to store word and character frequencies into an output text file
def StoreOutput(word_dic, char_dic):
    try:
        with open('output.txt', 'w') as file:
            # Write word frequencies to the output file
            file.write("Word Frequencies:\n")
            for k, v in word_dic.items():
                file.write(f"{k}: {v}\n")

            # Write character frequencies to the output file
            file.write("Character Frequencies:\n")
            for k, v in char_dic.items():
                file.write(f"{k}: {v}\n")
    except OSError as e:
        # Handle disk space full error
        if "No Space left on device" in str(e):
            raise DiskSpaceFullError("No space left on the device.")
    else:
        print("The inputted text has been processed and the output file has been saved.")

# Function to interact with the user, get file input, and process the file
def askuser():
    f = input("Enter the file name: ")  # Get the file name from the user
    parts = f.split()
    # Build the file path from input parts
    if len(parts) > 1:
        file_path = os.path.join(*parts)
    else:
        file_path = parts[0]

    file = pathlib.Path(file_path)  # Create a Path object for the file

    try:
        # Check if the file exists and process it
        if file.is_file():
            result = Processing_text_file(file)
            del result[1][' ']  # Remove spaces from character frequencies
            del result[1]['\n']  # Remove newlines from character frequencies
            StoreOutput(result[0], result[1])  # Store the results in a file
            showCloud(result[2])  # Display the word cloud
        else:
            raise FileNotFoundError(file)  # Raise error if file not found
    except FileNotFoundError as e:
        print(e)  # Print the error message

# Entry point of the program
if __name__ == "__main__":
    askuser()
