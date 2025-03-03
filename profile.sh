#!/bin/bash

# Function to create a new Firefox profile and open it
create_new_profile() {
    PROFILE_NAME="newprofile-$(date +%s)"
    firefox -CreateProfile "$PROFILE_NAME"
    firefox -P "$PROFILE_NAME" -no-remote &
    echo "$PROFILE_NAME" > current_profile.txt
}

# Call the function
create_new_profile
