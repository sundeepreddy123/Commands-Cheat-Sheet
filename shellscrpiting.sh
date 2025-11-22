1.Variables in shell
  * Declaring and using variables
name="sundeep"
age=28
echo "Name: $name"
echo "Age: $age"
      No spaces around = 
  * Variable Types
Type          Example
string        name="Ravi"
integer       num=5
Read-only     readonly pi=3.14
unset         unset name

  * User Input
read -p "Enter your nmme:" username
echo"Hello,$username!"
  ^ read is used to get input from user
  ^ -p allows prompting user inline.

  * Arithmetic Operations Basic Arithmetic
1.Basic Arithmetic
a=10
b=5
echo "sum =$((a + b))"
echo "Product = $((a * b))"
2.With expr
expr $a + $b
3.Floating-point (with bc)
echo "scale=2;5/3" | bc

  *Conditional statements
1.if statement
if [ $a -gt $b ]; then
  echo "$a is greater"
fi
if-Else
if [
    
