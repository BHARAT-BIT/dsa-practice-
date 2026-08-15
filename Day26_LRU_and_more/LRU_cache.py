# Only concetual part today as of Day 26 , real implementation on Day 32 
# Topic 1: LRU Cache — but INTRO only (not full implementation)

# Yeh sirf ek data structure nahi hai, yeh ek real system design problem hai jo tujhe interview mein baar baar milega. Concept-first approach:

# Problem kya hai: limited memory, unlimited data — kisko rakhein, kisko nikaalein?
# Naive solution (array/list se track karna) kyun slow hai — O(n) eviction, O(n) lookup
# Real insight: HashMap (O(1) lookup) + Doubly Linked List (O(1) insert/delete/reorder) ka combo kyun perfect hai — yeh samjhna zaroori hai, code baad mein
# Aaj sirf structure samjhenge — "kaise dono data structures ek dusre ko complement karte hain." Full implementation Day 32 mein karenge jab queue applications aayenge.