거꾸로 나열해도 동일한 숫자 판단하기

```PHP
class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        if ($x < 0 || $x % 10 === 0 && $x !== 0) {
            return false;
        }
        $str = strrev(strval($x));
        
        return intval($str) === $x;
    }
}
```

```PHP
class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        
        if ($x < 0 || ($x % 10 == 0 && $x != 0)) return false;

        $revertedNumber = 0;
        while($x > $revertedNumber) {
            $revertedNumber *= 10;
            $revertedNumber += fmod($x, 10);
            $x /= 10;            
        }
        
        return $x == $revertedNumber || $x == $revertedNumber / 10;
    }
}
```
