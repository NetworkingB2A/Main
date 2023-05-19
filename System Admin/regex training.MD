### What is the purpose of regular epressions?
It allows you to seach text and find infomation that you care about. 

### what is the basic regex
If you use a global flag it will allow you to match on anything that is in the string. If you take the global flag off, your regex will only match on the first time it finds that exact string.
/at/g < This will match any string part that has an at,

The f<b><i>at</i></b> c<b><i>at</i></b> ran down the street. The c<b><i>at</i></b> was searching for a mouse to e<b><i>at</i></b>.  

Symbol|What symbol means|
-|-
\+ | Match at least one but it can match more than one character 
? | Match an optional character 
\* | Match zero or more
\. | Match any single character, except for a new line
\ | The backslash cancels anything that comes after it. us it with a period to match a period as appose to a wildcard period
\w | Match any character
\W | Match anything that is not a character
\s | Match any form of white space
\S | Match anything that is not a white space
\w{min,max} | This will match on any word that is in the min and max numbers
\[any_character] | This will match any character that is inside the brackets, you can do ranges here.
any_character_1\|any_character_2 | This will search for the character on the left or ont the write.
(Group) | this will allow you to group portions of the regex.
^ | The carrot signifies the start of a line. If you only do the carrot, it will match on the first word of the line.
$ | The dollar sign signifies the end of the line. If you only do the dollar sign it will only match on the last word
^$ |  Carrot Dolar sign will match on the start and the end of the line.
(?<=) | This is called a positive look behind.
(?<!) | This is called a negitive look behind.