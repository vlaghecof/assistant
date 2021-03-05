"# assistant  Inteligent.Network.Assistant  " 

So basically this is just a simple assistant.
The project structure is as it follows 
 root :
        actions: here we define the functions that the 
                system can perform  
        Audio: the unit that allows your assistant to speak  
        Dispatcher : here we make the connection between the actions and the key words that
                     trigger them 
        settings: some global variables defined 
        
 The assistant can do the following
 
 open any website : keywords open name_here 
 
 search the web :  search what to be searched
 
 make a note:  take a note , make a note 
 
 get a space photo : space photo 
 
 system status : [default] system update 
 
 basic conversation module
 
 get a location : location place
 
 get a direction : from city1 to city2 
 
 create project(this one has a few variants): create project (this creates a folder in the default projects folder)   
                                              creates default project ( this one also crates a local git repo for the project)    
                                              create default git project (this one creates the remote git depo too)    
                                              (also when giving the name of the project you can specify a type(java python c) and it will
                                              also create a project in that language) 

Note: you can formulate the command however  you want as long as 
it contains the the trigger key words   
The Dispacher program uses the Sounder algorithm , which is a combination of 3 ALlgorithms.     
LEVENSTEIN EDIT DISTANCE is used to get an aproximation of how similar 
two words are.  
MUNKRES ALGORITHM , this  method is a combinatorial optimization algorithm that solves the assignment problem in polynomial.(How to distribute a series of task to obtain the minimum cost).    
METAPHONES , which is a way of grouping together the words that sound similar by indexing words by their English pronunciation.  
The acutal algorithm works on list of words , so we could have our dataset [[‘twitter’, ‘notifications’], [‘unread’, ‘emails’], …] , and the input query beeing : [‘give’, ‘twitter’, notifs’]. For each word in the query we compare it with the dataset using the Levenstein Distance , and save the result in a matrix .Now this matrix can used to compute the maximum assignment using Munkes algorithm, which takes the given algorithm and returns back the maximum scores index.This returned matrix is a vector matrix with the size of number of rows of the cost matrix (matrix that was sent to munkes algorithm) denoting which values gives the maximum output.
