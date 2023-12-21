import re

versions = [ "16.12(2r)",
"17.3(1r)",
"15.0(1r)SG15",
"17.03.04a",
"15.7(3)M8",
"15.2(7)E5",
"16.12.07",
"17.03.05",
"16.12.5",
"17.03.04b",
"15.2(2)E9",
"03.11.06E",
"15.2(7)E7",
"16.09.06",
"15.2(7)E4",
"16.7(1r)",
"16.12.08",
"15.2(4)E9",
"03.11.05.E",
"15.7(3)M6",
"15.2(4)E10",
"12.2(55)SE5",
"15.6(3)M9",
"15.2(7)E3",
"16.12.4",
"16.12.14",
"15.5(1)SY6",
"17.03.03",
"12.2(55)SE12",
"7.0(3)I7(10)",
"9.3(10)",
"17.03.06",
"17.10.01",
"17.06.04",
"16.06.10",
"16.03.11"]
#pattern we want to get checked against set to the compile method
#versionRegexChecker = re.compile(r'\d+\.\d+\.\d+\w?')  TestNumber1
versionRegexChecker = re.compile(r'\d+\.\d+\.\d+\w?')

for version in versions:
    versionRegexSearcher = versionRegexChecker.search(version)
    version_id = []
    if versionRegexSearcher is not None:
        for number in version.split('.'):
            if number.startswith('0'):
                version_id.append(number.lstrip('0'))
            else:
                version_id.append(number)
    updated_version = ".".join(version_id)
    print(updated_version)

#Match1 - Use as is subset - (^\d+\.\d+\(\d+\)[a-zA-Z]+\d+$) - eg. 15.7(3)M6 ([1+ digits].[1+ digits](1+ digit)[1+ a-z or A-Z]+[1+ digits]
#Match 2 - all double digit - use as is.. (^[1-9]\d+\.[1-9]\d+\.[1-9]\d+$) eg. 12.12.12
#Match 3 - Ones that we need to attempt as is + with dropping leading 0 - (?:(?:0)([1-9])) - eg. 03.03.05 - 
# Match 4- Ones that need to try as is + with added leading 0


# then you use the search method from the compile method and pass it the string you want to seach and see if you get a match.

# then you use the search method from the compile method and pass it the string you want to seach and see if you get a match.
#versionRegexSearcher = versionRegexChecker.findall(versions)
# the group is the matched object from the search function.
