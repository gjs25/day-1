function bottleSong(num) {
  while (num > 0) {
    if (num > 1) {
    console.log(`${num} bottles of beer on the wall, ${num} bottles of beer.
    Take one down and pass it around, ${(num = num-1)} bottles of beer on the wall.`)
    } else if (num === 1){
      console.log("1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, 0 bottles of beer on the wall.")
      break;
    }
  } 
 
}
(bottleSong(3)); //Because there is no return statement we do not need to console.log the fucntion. 
                //Because of how this function is structured it will implicitly be called with just the fucntion name and argument. 

