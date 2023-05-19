import re

This will search
re.search(r"regular_expression_pattern",  what_you_are_searching_through)

This will show you what you matched
re.search(r"regular_expression_pattern",  what_you_are_searching_through).group(0)

You can set a name of a match to a dictionary.

match = re.search(r"some_pattern (?P<the_pattern_name_variable>some_pattern_you_want_to_save)")
match.groupdict()


You can also use a flag that will allow you to use the ^ and $ on every line. the default behavior would start the ^ at the beginning of your file and the $ at the end of your file.  

re.search(r"regular_expression_pattern",  what_you_are_searching_through, flags=re.M)

the * symbols will not go past a new line character. To fix this issue you would set your flags=re.DOTALL

Some other methods you might want to use
- re.split()
- re.sub()
- re.findall()
