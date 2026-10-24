# Trees

Trees are recursive by construction. A tree problem usually asks for one of three things: a value returned from both children, a traversal order, or a property checked along a path.

Reach for recursion when the answer for a node can be assembled from the answers for its children. Reach for an explicit queue when the question is about levels. Reach for bounds or a previous value when the question is about ordering.

It assumes you can name the return contract for a subtree before writing the recursive call.
