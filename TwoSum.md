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
                return array($arr[$num], $key);
            }
            $arr[$val] = $key;
        }
        
    }
                                 
}
```
