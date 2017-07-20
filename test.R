
R version 3.2.5 (2016-04-14) -- "Very, Very Secure Dishes"
Copyright (C) 2016 The R Foundation for Statistical Computing
Platform: x86_64-w64-mingw32/x64 (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

> #----------------------------------------------
> #          1- ADDITION
> #-----------------------------------------------
> 
> add <- function (first,second) {
+    return (first + second)
+  }
>  first <- 5
>  
>  second <- 6
>    add(first, second)
[1] 11
> #-----------------------------------------------
> #       2- SUBTRACTION
> #-----------------------------------------------  
>    subtract <- function (first,second) {
+        return (first - second)
+  }
> first <- 10
>    
> second <- 2
> subtract(first,second)
[1] 8
> 
> #-----------------------------------------------
> #       3- MULTIPLICATION
> #-----------------------------------------------	
>   multiply <- function (first,second){
+        return (first * second)	
+  }
>  first <- 10
>  second <- 2
>  multiply(first,second)
[1] 20
> 
>  #-----------------------------------------------
>  #        4- DIVISION
>  #-----------------------------------------------
>  
>    divide <- function (first,second){
+         if (second == 0){
+             return ('inf')
+           }    
+         else{
+             return (first / second)
+           }
+       }
>   first <- 4
>   second <- 0
>   divide(first,second)
[1] "inf"
>   first <- 200
>   second <- 13
>   divide(first,second)
[1] 15.38462
>   
>   #-----------------------------------------------
>   #        5- EXPONENT
>   #-----------------------------------------------
>     exponent <- function (first,second){
+       
+       if (first != 0 && second ==1){
+         return (first) 
+       }  
+       else if (first == 0 && second >0){
+         return ("0")
+       }  
+       else if (first != 0 && second ==0){
+         return ("1")
+       } 
+       else if (first != 0 && second <0){
+         return ("For negative exponents, take the reciprocal of the base (flip it); change the negative exponent to a positive exponent and solve")
+       }
+       else
+         return (first ** second)
+     }
>   first <- 3
>   second <- 5
>   exponent(first,second)
[1] 243
>   
>   first <- 4
>   second <- 1
>   exponent(first,second)
[1] 4
>   
>   first <- 0
>   second <- 0
>   exponent(first,second)
[1] 1
>   
>   first <- 4
>   second<- 0
>   exponent(first,second)
[1] "1"
>   
>   first <- 5
>   second <- -4
>   exponent(first,second)
[1] "For negative exponents, take the reciprocal of the base (flip it); change the negative exponent to a positive exponent and solve"
>   
>   #-----------------------------------------------
>   #         6- SQUARE
>   #-----------------------------------------------
>   square <- function (first,second){
+        if (first == 0){
+            return (0)
+          }  
+        else if (second == 2){
+            return (first ** second)	
+          }
+      }
>    first <- 0
>    second<- 2
>    square(first,second)
[1] 0
>   
>   
>    first <- 2
>    second <- 2
>    square(first,second)
[1] 4
>    
>    first <- 9
>    second <- 2
>    square(first,second)
[1] 81
>    
>   #-----------------------------------------------
>  #           7- SQUARE ROOT
>   #-----------------------------------------------
>     squareRoot <- function (n){
+         if (n > 0){
+             return (n ** 0.5)
+           }  
+         else if (n == 0){
+             return (0)
+           } 
+         else if (n < 0){	
+             return ("inf")
+           
+             }
+       }
>     n <- 25
>     squareRoot(n)
[1] 5
>    
> 
>     n <- -10
>     squareRoot(n)
[1] "inf"
>     
>     #-----------------------------------------------
>     #         8- CUBE
>     #-----------------------------------------------	
>     
>     cube <- function (first,second){
+       if (first == 0){
+         return (0)
+       }  
+       else if (second == 3){
+         return (first ** second)	
+       }
+     }
>     first <- 0
>     second <- 10
>     cube(first,second)
[1] 0
>      
>      first <- 10
>      second <- 3
>      cube(first,second)
[1] 1000
> 
>     #-------------------------------------------------
>     #         9- COSINE
>     #-----------------------------------------------    
>      cosine <- function (first) {
+        second=math.cos(4)
+        return (second)
+      }
>      first <- 2
>      second <- 4
>      cos(second)
[1] -0.6536436
>      
>      
>      #-----------------------------------------------
>      #        10- MODULO
>      #-----------------------------------------------
>       modulo <- function(first, second){
+           return (first %%  second)
+         }
>      first<- 5
>      second <- 2
>        modulo(first, second)
[1] 1
>        
>        first<- 4
>        second <- 6
>        modulo(first, second)
[1] 4