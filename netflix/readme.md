# Data sets location
This directory contains three another ones related to the data sets and called **raw**, **processed**, **cleaned**. A description of each one is given below. 

## Raw directory
This directory contains original and immutable data sets. Do not edit your raw data, especially with Excel, open files only in read only mode. This directory contains four csv files, each one contains a part of the dataset. Each date file is structured as follows, however only the first one has an header :

- show_id : register ID
- type : type of video either movie or TV show
- title 
- director: The director of the movie 
- cast : casting
- country : where the movie/TV show come from 
- date_added : when it has been added to the netflix database
- release year : when it has been release
- rating 
- duration 
- listed_in : kind of video 
- description: a brief description 


## Processed directory
This directory contains intermediate transformed data sets. This working directory could contain multiple data sets.

## Cleaned directory
This directory contains canonical data sets could be used for publication. Theses data sets would be used for the analysis.
