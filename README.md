# MemoizationWithPython
This is a project to realise the principle of Memoization with Python

# Memoization function

  - def memoize(funcX, (funcX_arg1, funcX_arg2, funcX_3, ...., timeout_secs=5000)

   This function memoizes the results of any function . If resolver is provided,
 it determines the cache key for storing the result based on the arguments provided to the memorized function.

 - The first argument provided to the memorized function is used as the map cache key. The memorized values timeout after the timeout exceeds. The timeout is in defined in milliseconds.
 
 ## Example:
 ```
 def addToTime(year, month, day) {
   return Date.now() + Date(year, month, day)
  }
 
  result = memoize(addToTime, (year, month, day), 5000)
 ```

 ### Call the provided function, cache the result and return the value
 ```
 result = memoized(1, 11, 26); // result = 1534252012350
 ```
 
 ### Because there was no timeout this call should return the memorized value from the first call
 ```
  secondResult = memoized(1, 11, 26); // secondResult = 1534252012350
 ```
 ### After 5000 ms the value is not valid anymore and the original function should be called again
 ```
 thirdResult = memoized(1, 11, 26); // thirdResult = 1534252159271

```
 
 @param func      the function for which the return values should be cached
 @param resolver  if provided gets called for each function call with the exact same set of parameters 
                    as the original function, the resolver function should provide the memoization key.
 @param timeout   timeout for cached values in milliseconds
