# Project 5 - Baby Name Voyager
# CS 111, Reckinger
# Hiba Mirza
# November 5, 2022
# Plots historical data on the user-selected baby-names for the last 100 years

import matplotlib.pyplot as plt

# this function loads the file
def load_file(file_name):
  file = open(file_name)
  lines = file.readlines()
  # creates empty dictionary
  dictionary = {}
  max_pop = 0
  # iterates through each line
  for line in lines:
    # sets everything after the name, to a list (rankings)
    rankings = line.split()[1:]
    for i in range(len(rankings)):
      # changes all the strings in the list, to integers
      rankings[i] = int(rankings[i])
      # finds the max value of the entire file
      if rankings[i] > max_pop:
        max_pop = rankings[i]
    # at the start of every line, is a name
    name = line.split()[0]
    dictionary[name] = rankings
  for names in dictionary:
    # calls clean_data
    clean_data(dictionary[names], max_pop)
  file.close()
  return dictionary, max_pop

# only selects the specific data, depending on what the user inputs
def select_data(namestring):
  # splits the input into a list of names
  names = namestring.split(' ')
  # creates a new dictionary
  new_dictionary = {}
  # adds only the necessary data into the dictionary
  for i in range (len(names)):
    values = dictionary[names[i]]
    new_dictionary[names[i]] = values
  return new_dictionary

# this function plots the data
def plot_data(new_dictionary, namestring,max_value):
  plt.ion()
  # creates an empty string for the new file name
  newfilename = ''
  # increments years by 20
  years = range(1900, 2001, 20)
  names = namestring.split()
  # plots each point onto the graph
  for name in names:
    rankings = new_dictionary[name]
    plt.plot(
      rankings,
      "o"
      "--"
    )
    # adds every name to the empty string
    newfilename += name
  plt.legend(names)
  # creates ticks for x axis
  ticks = range(0, 11, 2)
  plt.xticks(ticks, years)
  # creates limit for y axis
  plt.ylim(max_value, -10)
  plt.xlabel("years")
  plt.ylabel("ranking")
  plt.title("Most Popular Baby Names, by decade")
  newfilename += '.png'
  # saves all plot data to the new file
  plt.savefig(newfilename)
  plt.show()
  return

# this function cleans the data
def clean_data(list, x):
  # goes through the list and replaces the 0's in the file
  for i in range(len(list)):
    if list[i] == 0:
      list[i] = x
  return list

# Main code below
if __name__ == '__main__':
    # prompts user for input
    namestring = input("Enter baby names: ")
    file_name = 'names-data.txt'
    # calls functions
    dictionary, max = load_file(file_name)
    plot_data(dictionary, namestring, max)