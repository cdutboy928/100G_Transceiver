# Project Requirements Document (PRD)

## Introduction

This project is a web data scraping application. Its primary function is to open a webpage using the Edge Dev browser, scrape specific numerical data from it, and save the data into a CSV file with two columns.

**Target Webpage:**

```
http://118.187.15.2:8089/#/sdn/business/business-info/Tunnel-Site-1688835019528867840%23Ne-1688854328804249600%23LINECARD-1-1%23PORT-1-1-C1-Site-1688835019101048832%23Ne-1688854328921690112%23LINECARD-1-1%23PORT-1-1-C1?tabKey=0
```

## Technologies Used

- **Python**
- **Selenium**
- **BeautifulSoup**
- **WebDriver**

## Core Functions

1. **Open the Target Webpage:**

   - Use the Edge Dev browser to navigate to the specified URL.
   - webpage login information: .env

2. **Parse HTML Content:**

   - Utilize BeautifulSoup to parse the HTML content retrieved from the webpage.

3. **Data Extraction:**

   - **First Numerical Value:**

     - **CSS Selector:**

       ```
       #cdk-overlay-2 > nz-modal-container > div > div > div.ant-modal-body.ng-tns-c213-13 > div > div.ant-col.ant-col-13 > div > pm-list-panel > nz-tabset > div > div.ant-tabs-tabpane.ng-star-inserted.ant-tabs-tabpane-active > div > nz-table > nz-spin > div > div > nz-table-inner-default > div > table > tbody > tr:nth-child(4) > td:nth-child(2)
       ```

     - **HTML Element:**

       ```html
       <td _ngcontent-ene-c670="" class="ant-table-cell">14.44</td>
       ```

     - **Description:**

       - Extract the numerical value `14.44` from the specified `<td>` element.

   - **Second Numerical Value:**

     - **CSS Selector:**

       - *(To be provided; specify the exact CSS selector for the second value.)*

     - **HTML Element:**

       - *(To be provided; include the HTML snippet containing the second value.)*

     - **Description:**

       - Extract the second numerical value from the specified element.

   - **Additional Values:**

     - Repeat the above steps for any additional numerical values that need to be extracted.

4. **Save Data to CSV:**

   - Compile the extracted numerical values into a CSV file.
   - The CSV file should have two columns corresponding to the extracted values.

## File Structure

The project will maintain simplicity by using a minimal file structure.

```
your_project/
│
└── scrape.py
```

- **`scrape.py`:**

  - This is the main Python script that contains all the code necessary for the project.
  - Responsibilities include:
    - Opening the webpage.
    - Parsing the HTML content.
    - Extracting the specified data.
    - Saving the data to a CSV file.

## Documentation and Guidelines

### 1. Setup and Configuration

- **WebDriver:**

  - Ensure the Edge WebDriver is downloaded and correctly configured.
  - Specify the path to the WebDriver in the script.

- **Dependencies:**

  - Install the required Python libraries:
    ```
    pip install selenium beautifulsoup4
    ```

### 2. Script Workflow

- **Initialize WebDriver:**

  - Use Selenium to initialize the Edge Dev browser with the specified WebDriver.

- **Navigate to URL:**

  - Direct the browser to open the target webpage.

- **Wait for Page Load:**

  - Implement a mechanism to wait for the page to fully load.
    - This can be a simple `time.sleep()` or a more robust `WebDriverWait` from Selenium.

- **Retrieve Page Source:**

  - Obtain the HTML content of the page after it has fully loaded.

- **Parse HTML with BeautifulSoup:**

  - Use BeautifulSoup to parse the retrieved HTML content.

- **Data Extraction:**

  - Utilize the provided CSS selectors to locate the specific HTML elements containing the numerical values.
  - Extract and clean the data (e.g., remove whitespace, convert to numerical types if necessary).

- **Error Handling:**

  - Implement checks to ensure that each element is found before attempting to extract data.
  - Handle exceptions gracefully, providing informative error messages.

- **Save to CSV:**

  - Open/Create the output CSV file.
  - Write the extracted data into the CSV file in the specified format.

- **Close Browser:**

  - After data extraction is complete, ensure the browser session is properly closed.

### 3. Example Code Snippet

*Note: The following is a conceptual example to illustrate the approach and should not be used as actual code.*

```python
# Import necessary libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

# Configure WebDriver path
driver_path = 'path/to/your/edgedriver'  # Replace with your actual WebDriver path

# Initialize WebDriver for Edge
browser = webdriver.Edge(executable_path=driver_path)

# Open the target webpage
browser.get('http://your_target_url')  # Replace with the actual URL

# Wait for the page to load completely
time.sleep(5)  # Adjust the sleep time as necessary

# Get the page source
page_source = browser.page_source

# Parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Extract the first value using the CSS selector
value1_element = soup.select_one('#your_css_selector')  # Replace with actual selector
if value1_element:
    value1 = value1_element.text.strip()
else:
    value1 = None  # Handle the case where the element is not found

# Repeat extraction for additional values...

# Save the data to a CSV file
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Value1', 'Value2'])  # Include headers as necessary
    writer.writerow([value1, value2])      # Replace with actual variables

# Close the browser
browser.quit()
```

### 4. Important Considerations

- **Dynamic Content Loading:**

  - If the webpage loads content dynamically (e.g., via JavaScript), ensure that the script waits for the necessary elements to be present before attempting to parse the HTML.
  - Use Selenium's `WebDriverWait` and `ExpectedConditions` to wait for elements.

- **CSS Selectors Accuracy:**

  - Verify that the provided CSS selectors accurately locate the desired elements.
  - Be aware that complex selectors might be brittle; consider simplifying them if possible.

- **Data Validation:**

  - Implement validation checks on the extracted data to ensure it meets expected formats and ranges.

- **Exception Handling:**

  - Use try-except blocks around critical operations to catch and handle exceptions.
  - Log errors or issues to a file or console for debugging purposes.

- **Code Modularity:**

  - While the project aims to use a single script for simplicity, consider organizing the code into functions or classes within `scrape.py` for better readability and maintainability.

### 5. Future Enhancements

- **Scalability:**

  - If the project scope expands, consider refactoring the code to accommodate additional features or handle more complex data extraction tasks.

- **Configuration File:**

  - Externalize configurations (like URLs, selectors, file paths) into a separate file or use command-line arguments for flexibility.

- **Logging:**

  - Implement a logging mechanism to track the script's execution flow and record any issues encountered.

## Deliverables

- **`scrape.py` Script:**

  - A fully functional Python script that performs all the tasks as outlined.

- **`output.csv` File:**

  - The CSV file containing the extracted numerical values in the specified format.

## Developer Guidelines

- **Code Quality:**

  - Write clean, readable, and well-documented code.
  - Follow Python coding standards (PEP 8).

- **Testing:**

  - Test the script thoroughly to ensure it handles different scenarios, including missing elements and network issues.

- **Dependencies Management:**

  - List all dependencies and their versions.
  - Use a virtual environment to manage packages if necessary.

- **Version Control:**

  - Use a version control system (like Git) to track changes to the script.
  - Commit code with clear messages explaining the changes.

## Summary

This document provides a comprehensive overview of the web data scraping project, outlining all necessary details to ensure clear alignment among developers. The project focuses on simplicity and efficiency, using a single Python script to perform all tasks. By adhering to the guidelines and utilizing the provided resources, developers should be able to implement the project effectively.

---

**Note:** This PRD includes all the necessary details, file structure, and documentation to guide developers in implementing the project without providing actual code. The example code snippets and explanations serve as important context and should be used for reference purposes only.