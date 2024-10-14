Baby Name Voyager - Visualizing Baby Name Trends

About (Baby Name Voyager)
The Baby Name Voyager is an interactive application designed to visualize historical trends of baby names over the past century. By plotting the popularity of user-selected names from a dataset, this program provides an engaging way to explore how the popularity of names has changed over the years.

Key Features:
Historical Data Visualization: Users can select one or more baby names to see their popularity trends plotted over a 100-year period, helping to understand naming trends over time.

Interactive Plotting: The application uses Matplotlib to create dynamic plots that display the rankings of selected names, making the data visually accessible and easy to interpret.

Data Cleaning Mechanism: The application automatically replaces zero rankings (indicating no data) with the maximum ranking from the dataset, ensuring accurate representation in the plots.

Customizable Input: Users can enter any combination of names to generate personalized plots, enhancing the application’s flexibility and user engagement.

How It Works:
The application loads baby name data from a text file, processing rankings for names from 1900 to 2000.
Users are prompted to input the names they wish to visualize.
The application filters the dataset to select only the requested names and prepares the data for plotting.
The application utilizes Matplotlib to create a visual representation of the selected names' popularity, showing changes in rankings across decades.

How to Run It:
Ensure you have Python installed on your machine.
Install the Matplotlib library by running:
bash
pip install matplotlib
Download the project files, including main.py and the necessary names-data.txt file containing historical baby name data.
Open main.py in your preferred Python IDE or text editor.
Run the main.py script. Follow the prompt to enter the desired baby names, and the application will display the popularity trends for those names.

In summary, the Baby Name Voyager is a unique tool that combines data visualization and historical insight, providing users with an informative and interactive experience in exploring baby name trends. It highlights the shifts in naming conventions and the cultural influences that shape these trends over time.
