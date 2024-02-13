#!/bin/bash

# the goal of this is to install the dependednces from the LinuxGSM game server game you want to intall, from the github pages of LinuxGSM, this way if there are update to the dependencies they will be taken care of with out manual intervention of WebGSM.
# Path to the CSV file
CSV_FILE="https://github.com/GameServerManagers/LinuxGSM/blob/master/lgsm/data/debian-12.csv"

# Read records from the CSV file (excluding the header)
while read -r line; do
    # Extract the first column (package name)
    package_name=$(echo "$line" | cut -d ',' -f 1)

    # Add your logic here to handle the package name
    # For now, let's just print it
    echo "Package name: $package_name"
done < <(tail -n +2 <(curl -s "$CSV_FILE"))

# Note: The 'curl -s' command fetches the CSV file content
# The 'tail -n +2' command skips the header line
# The 'cut -d ',' -f 1' command extracts the first column
