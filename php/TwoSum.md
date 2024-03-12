# 배열 $nums 의 두 값의 합이 $terget이 되는 key를 배열로 반환하기


solution1
```PHP
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $count = count($nums);
        for ($i= 0; $i < $count - 1; $i++) {
            for ($j = 1; $j < $count; $j++) {
                if ($nums[$i] + $nums[$j] === $target) {
                     return [$i, $j];
                }
            }
        }
    }
}
```

solution2
```PHP
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $result = [];
        foreach ($nums as $i => $val) {
            $num = $target - $val;
            if ($j = array_keys($nums, $num)) {
                return [$i, $j[0]];
            }
        }
    }
}
```

solution3
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
