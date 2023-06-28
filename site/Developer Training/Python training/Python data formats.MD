### How to open a file
** Remember to always close any file that you have opened **
If you would like to have the file close automatically once your are done with it, use the with open context manager.

variable_name = open("file_name.txt", "file_argument")

file arguments include the following
- r : open for reading
- w : open for writing
- x : open for exclusive creation, failing if the file already exists
- a : open for writing, appending to the end of the file it is exists
- b : open in binary mode
- t : open in text mode
- \+ : open for updating (reading and writing)

## Parsing Data
### Comma-Separated Values (CSV)
Python has a built-in CSV module.
I highly recommend that you use a CSVDictReader to read data from a CSV File.
This will take to top line of your CSV and the current next line down, converting it into a dictionary. converting this data into a dictionary will make you life easier as you get farther in your program.  
### JavaScript Object Notation (JSON)
JSON is build around a key/value pairing. JSON is used a lot in web services.
JSON and Python dictionaries/lists are identical. Python dictionary is a JSON object, Python list is a JSON array.  
White space does not matter for the Python code to read the data.
There are four main functions you will use when working with Python and JSON.
  (** The s at the end of the function name means string. **)
- load() : This allows you to import native JSON and converts it to a Python dictionary from a file.
- loads() : This will import JSON from a string for parsing and manipulating within your program.
- dump() : This is used to write JSON data from Python object to a file. You would use this to produce more machine readable code.
  - You can set dump ( sort_keys = True, indent = 4) and this will also make your output more readable.
- dumps() : This allows you to take JSON dictionary data and convert it into a serialized string for parsing and manipulating with Python. You would use this this to have the output be more human readable.
### Extensible Markup Language (XML)
XML works hand and hand in HTML.  
XML has a tree structure. with the root element being at the very top.  
All XML works with tags. All data resides in these tags <>, </>.  
Understanding XML is important as some protocols/standards work exclusively with XML. Without understanding XML NETCONF with YANG will be difficult to use.  
XML is one of the more difficult markup languages to learn.  
You can use xmltodict in Python to help you work with the XML data.  
You can also use the XML unparse function to make the data easier to read.
White space does not matter here.
#### XML Namespaces
XML is very popular and has been used on the internet for many years. You will likely run into an issue were you have two different systems that have the same tag names but they represent different data. This is where XML namespaces and prefixes comes into play.
A prefix is an alphabetic character or a string put before the actual tag name followed by a colon.

when using XML prefixes you also need to make sure you define namespaces for those prefixes. the name of a namespace is a URI. Namespaces are defined with the xmlns attribute in the starting tag.
<a:table>
  <a:tr>
    <a:td>router</a:td>
    <a:td>switch</a:td>
  </a:tr>
</a:table>
<b:table>
  <b:tablerow>
    <b:tabledata>router</b:tabledata>
    <b:tabledata>bananas</b:tabledata>
  </b:tablerow>
</b:table>
### YAML Ain't Markup Language (YAML)
YAML is a popular human-readable format for constructing configuration files.
Tools like Ansible use YAML files everywhere.
White space is very important and your YAML files will break if your white space is off.  
Use the PyYaml Module in Python to work with YAML files.  
The two main functions you will use are load() and dump().
