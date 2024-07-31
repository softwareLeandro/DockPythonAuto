# DockPythonAuto

This project uses Selenium and Pyautogui to automate navigation on a product prices website, loading all products, and uploading a price spreadsheet.

## Technologies Used

- **Selenium**: To automate browser navigation and interactions.
- **Pyautogui**: To interact with the user interface, especially to handle system dialog boxes.

## Automated Steps

1. Enter the website.
2. Scroll the entire page down to load the products and click "Load More" to view the remaining products.
3. Scroll the page all the way down again.
4. Scroll back up to the top.
5. Click the "Upload Price Spreadsheet" button.
6. Upload the `precos-produtos-atualizados.xlsx` spreadsheet.


## How to Run

1. **Prerequisites**:
    - Python 3.x
    - Selenium
    - Pyautogui
    - ChromeDriver compatible with your Google Chrome version
    - A configured Chrome profile (update the profile path in the code as needed)

2. **Install Dependencies**:
    ```bash
    pip install selenium pyautogui
    ```

## Considerations

- **Verify XPATH**: Make sure the XPATH selectors used to locate the buttons are correct and match the elements on the page.
- **Wait Times**: The wait times (`sleep`) may need to be adjusted depending on your system and network speed. If the Finder dialog takes longer to open, increase the wait time.
- **macOS Permissions**: Ensure that `pyautogui` has the necessary permissions on macOS to control the user interface. Go to `System Preferences > Security & Privacy > Privacy > Accessibility` and add your terminal or IDE to the list of allowed applications.


## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.
