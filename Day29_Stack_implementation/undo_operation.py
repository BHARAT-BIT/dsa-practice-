#only conceptual 

# Real-world twist: jab tu pop karta hai (undo), to woh action gayab nahi ho jaana chahiye permanently — kya hoga agar user Redo (Ctrl+Y) bhi karna chahe? Undo ke baad agar mann badle aur wapas chahiye woh action?

# Iske liye trick yeh hai — do stacks use karte hain:

# undo_stack — jahan saari operations push hoti hain
# redo_stack — jab bhi tu undo_stack se pop karta hai (undo), us item ko redo_stack mein push kar do


# Redo stack clear ho jaana chahiye jaise hi user koi naya operation kare undo ke baad. Kyun? Socho:

# Tune "Hello World" type kiya
# Undo kiya do baar → "Hello" reh gaya (redo_stack mein "W", "o"... wagera pending hain)
# Ab tune naya likha "Hello Bharat"

# Ab agar Redo dabaye to kya hona chahiye — "World" wapas aana chahiye? Nahi, kyunki tu ek naye timeline pe chala gaya hai. Woh purana "World" wala future ab invalid ho gaya — jaise time travel movie mein naya branch bante hi purana future mit jaata hai.

# To rule ban gaya: naya operation aaye to redo_stack.clear().