# atos-unihack-2020
Atos Unihack 2020 Speed Code Challenge

This is a Speed Code Challenge for Unihack 2020.

Simple problem where we want a simple and elegant solution.
You can write the code in any coding language. 
If any build/compiling is required, please insert a build script
You have one hour to commit in your branch.
The winning solution will be pushed to main branch.

---- Problem ---- 
A Petri net, also known as a place/transition (PT) net, is one of several mathematical modeling languages for the description of distributed systems. It is a class of discrete event dynamic system. A Petri net is a directed bipartite graph that has two types of elements, places and transitions, designed to passthrough informational containers called tokens. A place can contain any number of tokens. A transition is enabled if all places connected to it as inputs contain at least one token. 

More informations about Petri nets can be found here: https://en.wikipedia.org/wiki/Petri_net#:~:text=A%20Petri%20net%20is%20a,contain%20at%20least%20one%20token..

Task:
Create a functional program that simulates a Petri net that is not accounting transport capacity, only node (Place) capacity.
Addition: Each entity (Place, Transition, Token) shall contain a record of interaction, in such way that at any given time, on a selected entity it can be visible the entity log.


---- Instructions -----
1. Create your own FORK of this repository
2. Solve the problem in any programming language, at your convinience
3. Push the solution to your fork.

---- Considerations -----
Only pushes to the announced hour will be considered

### Running 

Everything is contained in a python script, just give it a `python ./petri/petri.py`. 

Modify stuff in `input_data.py` and make sure you have `TRANSITIONS` defined. At every tick all transitions happen (if possible) and then the changes are propagated all at once.

If you added a recursive (infinite) net then you can just pass `--iterations`.

