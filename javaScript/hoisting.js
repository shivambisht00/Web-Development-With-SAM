// hoisting is a behavioor in  js where declaration are moved to the top of there scope during the compilation phase , before the code is executed 


test();// => prints the function
console.log(x);//=> prints the undefined 
console.log(test);//=> prints the whole function 

var x = 7;
function test(){
    console.log("i am shiavm ");
}
