# Joy Generator

Joy Generator is a simple Python script that repeatedly prints the word "Joy" on the same line in the console. It continues running until the user manually stops it with `Ctrl + C`. This script can be used as a basic template for more complex looping tasks or just to spread a little joy in your terminal!

## Features
- Prints "Joy" repeatedly on the same line.
- Configurable delay between prints.
- Graceful exit when interrupted.

## Requirements
- Python 3.x
- Git

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/j0yk3r/joy-generator.git
   cd joy-generator
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Run the script:

   ```bash
   python3 joy_generator.py
   ```

To stop the script, press `Ctrl + C`.

## Customization

- **Delay between prints:** The delay is set to 0.1 seconds by default. You can adjust the `time.sleep(0.1)` value in the script to change the speed at which "Joy" is printed.
- **Word to print:** The script prints "Joy" by default. To print a different word, replace `"Joy"` in the `print()` function with your preferred word.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
