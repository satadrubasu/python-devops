## GREP ##

|Description|Command|
|---|---|
|print 2 lines above and 2 lines below after a pattern grep|grep -B 2 -A 2 --color 'keyword' /path/to/file.log|


## SED ##

* for Mac add     '' -e  ( single quote X 2 )
> sed -i '' -e "/keyword/d" file.txt

Note: the sed command prints the contents of the file on terminal by removing the lines.To Remove the lines from the source file itself, use the -i option with sed command.
> sed -i '1d' file

###  Sed Command to Delete Lines - Based on Pattern Match
In the following examples, the sed command deletes the lines in file which match the given pattern.

1. Delete lines that begin with specified character
> sed '/^u/d' file

^ is to specify the starting of the line. Above sed command removes all the lines that start with character 'u'.

2. Delete lines that end with specified character
> sed '/x$/d' file

$ is to indicate the end of the line. The above command deletes all the lines that end with character 'x'.

3. Delete lines which are in upper case or capital letters
> sed '/^[A-Z]*$/d' file

4. Delete lines that contain a pattern
> sed -i '/debian/d' file


