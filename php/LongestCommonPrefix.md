연속으로 중복되는 문자 출력하기

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Solution 1
Horizontal scanning
```PHP
class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        
        if (count($strs) < 1) {
            return '';
        }
     
        if (count($strs) === 1) {
            return $strs[0];
        }

        $compare = $strs[0];
        
        $prefix = '';
        foreach($strs as $key => $str) {
            
            if ($key < 1) {
                continue;
            }
            if ($key > 1) {
                $compare = $prefix;
                $prefix = '';
            }
            for($i = 0; $i < strlen($compare); $i++) {
                if (!isset($str[$i]) || $compare[$i] !== $str[$i]) {
                  break;  
                } 
                $prefix .= $str[$i]; 
            }
            if (empty($prefix)) {
                return '';
            }
        }
        return $prefix;
    }
}

```

solution2
Vertical scanning

```PHP
class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        
        if (count($strs) < 1) {
            return '';
        }
     
        $strs_len = count($strs);
        if ($strs_len === 1) {
            return $strs[0];
        }

        $prefix = '';
        $compare = $strs[0];

        for($i=0; $i<strlen($strs[0]); $i++) {
            for($j=1; $j<$strs_len; $j++) {
                
                if ($compare[$i] !== $strs[$j][$i]) {
                    return $prefix;
                }
                
                if ($compare[$i] === $strs[$j][$i] && $strs_len - 1 === $j) {
                    $prefix .= $strs[$j][$i];
                }
            }
        }

        return $prefix;
    }
}
```



