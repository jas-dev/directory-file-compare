# My collection of python automation modules

This is the begining of my python modules collection for automating common daily tasks. In the past, I've developed similar collections at work but I keep work and personal content well separated.

## File hashing, directory comparison, and file operations 

### The problem
I work with sizeable data sets, both personally and professionally. I value staying organized, and I have an effective data management system. But, my directories trees are filled with categorized files of different data clasifications, and working with them is too time consuming without using automation.

* I need to compare and modify directories often 
* I need to do batch file opertaions often
* I need to pivot on single or multiple artifacts often as part of research & analysis that requires enrichment
* I dislike repeating myself (DRY principle) and wasting time
* I need to programatically interact with various platforms and services
* I often need to do all the above as part of a larger application

### The solution
Here I have my intial collection, just a few functions I can import or call from cli as needed to generate MD5 hashes for individual files or recursively for all files in a directory tree, compare for duplicates and uniques, aggregate and list paths, output to line separated text file, and take further action from there (for now just delete). 

#### To do:
* Change the relative pathing text file output to absolute pathing, which is more useful overall and safer for deletion operations (beware when deleting stuff!)
* Implement optional interactive cli workflow 

### Modules on my backlog:

* API requests/interactions
* Bootstrapping various processes
* Analysis and reporting
* Other data cleaning and transformation
* OS automations
* Networking tools
