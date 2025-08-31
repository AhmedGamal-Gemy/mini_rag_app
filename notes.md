# General Notes 
1. You can make git leave out certain files and folders and you can put all these files in a folder named assets.
2. The configs are typically placed in .env like project name or an api secret key. and typically all capital and _ between the word. and the configs is either string or number only.
but this only can make errors because there's no file .env tracked in git. To solve this you should make an exact copy of it and name it .env.example without any secrets of course like api key 

# In requirements notes 
1. Leave a line in the end of the file. (If you didn't do this and when anyone add another package he will make a new line (\n) so the previous line go updated as well )
2. Don't ever leave the package without version ( you can find any package version when searching like this 'fastapi pypi')
  