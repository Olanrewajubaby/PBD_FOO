#----------------------------------------------
#          1- ADDITION
#-----------------------------------------------

add <- function (first,second) {
   return (first + second)
 }
 first <- 5
 
 second <- 6
   add(first, second)
#-----------------------------------------------
#       2- SUBTRACTION
#-----------------------------------------------  
   subtract <- function (first,second) {
       return (first - second)
 }
first <- 10
   
second <- 2
subtract(first,second)

#-----------------------------------------------
#       3- MULTIPLICATION
#-----------------------------------------------	
  multiply <- function (first,second){
       return (first * second)	
 }
 first <- 10
 second <- 2
 multiply(first,second)

 #-----------------------------------------------
 #        4- DIVISION
 #-----------------------------------------------
 
   divide <- function (first,second){
        if (second == 0){
            return ('inf')
          }    
        else{
            return (first / second)
          }
      }
  first <- 4
  second <- 0
  divide(first,second)
  first <- 200
  second <- 13
  divide(first,second)
  
  #-----------------------------------------------
  #        5- EXPONENT
  #-----------------------------------------------
    exponent <- function (first,second){
      
      if (first != 0 && second ==1){
        return (first) 
      }  
      else if (first == 0 && second >0){
        return ("0")
      }  
      else if (first != 0 && second ==0){
        return ("1")
      } 
      else if (first != 0 && second <0){
        return ("For negative exponents, take the reciprocal of the base (flip it); change the negative exponent to a positive exponent and solve")
      }
      else
        return (first ** second)
    }
  first <- 3
  second <- 5
  exponent(first,second)
  
  first <- 4
  second <- 1
  exponent(first,second)
  
  first <- 0
  second <- 0
  exponent(first,second)
  
  first <- 4
  second<- 0
  exponent(first,second)
  
  first <- 5
  second <- -4
  exponent(first,second)
  
  #-----------------------------------------------
  #         6- SQUARE
  #-----------------------------------------------
  square <- function (first,second){
       if (first == 0){
           return (0)
         }  
       else if (second == 2){
           return (first ** second)	
         }
     }
   first <- 0
   second<- 2
   square(first,second)
  
  
   first <- 2
   second <- 2
   square(first,second)
   
   first <- 9
   second <- 2
   square(first,second)
   
  #-----------------------------------------------
 #           7- SQUARE ROOT
  #-----------------------------------------------
    squareRoot <- function (n){
        if (n > 0){
            return (n ** 0.5)
          }  
        else if (n == 0){
            return (0)
          } 
        else if (n < 0){	
            return ("inf")
          
            }
      }
    n <- 25
    squareRoot(n)
   

    n <- -10
    squareRoot(n)
    
    #-----------------------------------------------
    #         8- CUBE
    #-----------------------------------------------	
    
    cube <- function (first,second){
      if (first == 0){
        return (0)
      }  
      else if (second == 3){
        return (first ** second)	
      }
    }
    first <- 0
    second <- 10
    cube(first,second)
     
     first <- 10
     second <- 3
     cube(first,second)

    #-------------------------------------------------
    #         9- COSINE
    #-----------------------------------------------    
     cosine <- function (first) {
       second=math.cos(4)
       return (second)
     }
     first <- 2
     second <- 4
     cos(second)
     
     
     #-----------------------------------------------
     #        10- MODULO
     #-----------------------------------------------
      modulo <- function(first, second){
          return (first %%  second)
        }
     first<- 5
     second <- 2
       modulo(first, second)
       
       first<- 4
       second <- 6
       modulo(first, second)
       
       
     