---
layout: post
title: new-autoposter
date: 2023-05-21 02:48 -0400
---


I made an autoposter if you want to see it. It makes writing posts with jekyll sooooooo much easier and autocommits everything. 
```
#!/bin/bash
# Rhett Applestone

# Check if Jekyll is installed
if ! command -v jekyll &> /dev/null; then
    echo "Jekyll is not installed. Please install Jekyll and try again."
    exit 1
fi

# Check if Micro text editor is installed (delete this part if you want to use like vim)
if ! command -v micro &> /dev/null; then
    echo "Micro text editor is not installed. Please install Micro and try again."
    exit 1
fi

#Delare post name variable
post_name=$(echo "$1" | sed 's/ /-/g')

# Set the Jekyll directory
dir=PUT YOUR DIR HERE

# Change into that dir
cd $dir

# Create the new post
jekyll post "$post_name"

# Get date as a variable
date=$(date +%Y-%m-%d)

# Open the post in Micro text editor (could be any editor)

micro _posts/"$date"-"$post_name".md

# Change to the Jekyll dir on exit
cd $dir || exit

# Push changes
git add .
git commit -m "$post_name"
git push
```

Check github for newest code
