# About

The purpose of the script is to compare two text files which are expected to be the same.
The script will create a report and mark the differences, if any.

# Versions

V1.0 
	- 6/22/2023 First commit


# How to run

1. Put pair of files that needs to be compared into the /Config directory.
Make sure both file names starts with the same prefix length (default prefix length is 8 characters). Prefix length can be changed using "file_name_prefix_length" variable

Example:
casant01-rccdnslb-01
casant01-rccdnslb-02

Both files has the same prefix length of 8 charactes "casant01"

You can put multiple files altogether under /Config directory, the script will compare all pairs of filenames which name starts with the same 8 characters and create separate reports.

2. Run the script

python3 config_diff.py

3. Review report under /Report directory