```PHP
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
    
        $arr = array();
        
        foreach($nums as $key => $val) {
            $num = $target - $val;
            
            if(isset($arr[$num])) {
                if ($key === $arr[$num]) {
                    continue;
                }
                return array($arr[$num], $key);
            }
            $arr[$val] = $key;
        }
        
    }
                                 
}
```
