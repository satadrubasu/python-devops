

## SED ##


Note: the sed command prints the contents of the file on terminal by removing the lines.
    However the sed command does not remove the lines from the source file. To Remove the lines from the source file itself, 
use the -i option with sed command.
> sed -i '1d' file

If you dont wish to delete the lines from the original source file you can redirect the output of the sed command to another file.
sed '1d' file > newfile

###  Sed Command to Delete Lines - Based on Pattern Match
In the following examples, the sed command deletes the lines in file which match the given pattern.

1. Delete lines that begin with specified character
> sed '/^u/d' file
linux
fedora

^ is to specify the starting of the line. Above sed command removes all the lines that start with character 'u'.

2. Delete lines that end with specified character
> sed '/x$/d' file
fedora
debian
ubuntu

$ is to indicate the end of the line. The above command deletes all the lines that end with character 'x'.

3. Delete lines which are in upper case or capital letters
> sed '/^[A-Z]*$/d' file

4. Delete lines that contain a pattern
> sed '/debian/d' file
linux
unix
fedora

5. Delete lines starting from a pattern till the last line
> sed '/fedora/,$d' file
linux
unix

Here the sed command removes the line that matches the pattern fedora and also deletes all the lines to the end of the file which appear next to this matching line.

6. Delete last line only if it contains the pattern
> sed '${/ubuntu/d;}' file
linux
unix
fedora
debian

Here $ indicates the last line. If you want to delete Nth line only if it contains a pattern, then in place of $ place the line number.

