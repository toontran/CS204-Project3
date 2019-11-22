# Project 3 Phase 2
### By: Sam Citron, Amanda Christy, Arsh Noor Amin, and Tung Tran

For this phase, we started by creating our MinHeap along with our MinHeap visualization in Bridges. MinHeap had a sift up and sift down method, as we had to check to make sure the value in each internal node was smaller than or equal to the values in the children of that parent node. Our MinHeap class held Priority as a key and dispatch string as a Value, and contained a sorting method where it would sort the heap. In order to visualize our MinHeap, we used Bridges again. The following is a visualization of the MinHeap in Bridges:

http://bridges-cs.herokuapp.com/assignments/3/tungtran

Our old visualizations from Phase 1 were that we displayed our 2 AVL Trees in Bridges which had some labels but were not color coded. In this Phase, however, we updated these old AVL visualizations in Bridges so that they looked more organized and were easier to read as well as color coded, as shown here:

http://bridges-cs.herokuapp.com/assignments/1/tungtran (crime tree)

http://bridges-cs.herokuapp.com/assignments/0/tungtran (location tree)

Another cool visualization that we added for creativity was that we used ipyleaflet in order to show the surrounding area of our dispatch coordinates on a realistic looking map of Chicago. ipyleaflet is an interactive map in the Jupyter notebook, and an example visualization of what a group of four coordinates would look like on the map is shown below:

In addition to these visualizations, we also created a few new methods in main that added a dispatch to our dispatch queue, located the coordinates of the surrounding area, and decided where to send the next patrol using tuples. Our code for these methods involved creating a "total priority" value (our beat priority + our IUCR priority) to insert into our dispatch queue that helped us make a decision where we wanted our dispatch location to be. We found the location of our surrounding area by creating 4 different coordinate points then using that location area to get a set of four tuples. The tuples created an area around our BEAT. Lastly in main, we also added a method to decide the next location we wanted to patrol. We checked to see what dispatch string was popped off in the MinHeap class to get the location we needed to go to. If the dispatch queue was empty, however, we would read the csv file over again, determine the priority of the dispatch string, and create and sort a list of key-value pairs (key is the total priority and value is the location area).

We tested our code by running in the Terminal then clicking on the generated links from Bridges to make sure our visualizations were accurate. In order to initially test the ipyleaflet code online, we just picked random coordinates and ensured it made bounds on the map then we used it with our actual datat to make sure it worked. For most of the project we would write our code in Repl so we could all work on it, then one of us would create .py files of it all then run it on the Terminal to see if everything worked together.
