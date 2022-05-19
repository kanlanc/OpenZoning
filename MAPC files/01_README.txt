Shapefiles and metadata were downloaded from https://zoningatlas.mapc.org/ on 
May 19, 2022.

Since the shapefiles may exceed 100MB, they are not included in the remote 
GitHub repo. You may choose to add them to the MAPC files folder in your 
local repo (the .gitignore file assumes that's what you've done). The script in
code/read-MAPC.R reads those shapefiles and saves them as the parquet files you 
see here. 

Actually, the shapefiles for the overlay districts are not too big to just keep 
on GitHub, it's just the base district file that's too big as the moment. Carole
didn't see any need to treat them differently though.
