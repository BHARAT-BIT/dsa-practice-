def pathsum(root,target):

    def has_sum(root,current_sum):
        if not root:
            return False 

        current_sum += root.val 

        if not root.left and not root.right:
            return current_sum == target 
        
        return has_sum(root.left , current_sum) or has_sum(root.right , current_sum)