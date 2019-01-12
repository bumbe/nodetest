/*
Pushbutton med node.js
button inkopplad via 1 Kohm från GPIO 23
LED inlopplad till GPIO 18
Om status=0 så tänds LED (=button presses)
Om status=1 så släcks LED (=button released)
*/
var Gpio = require('onoff').Gpio; //include onoff to interact with the GPIO
var LED = new Gpio(18, 'out'); //use GPIO pin 4 as output
var pushButton = new Gpio(23, 'in', 'both'); //use GPIO pin 23 as input, and 'both' button presses, and releases should be handled

pushButton.watch(function (err, value) { //Watch for hardware interrupts on pushButton GPIO, specify callback function
  console.log(value);	// The current state of the pin
  if (err) { //if an error
    console.error('There was an error', err); //output error message to console
  return;
  }
  if (value==0) {
  LED.writeSync(1); 
  }   //turn LED on or off depending on the button state (0 or 1)
 else if (value==1){
  LED.writeSync(0); 
  //turn LED on or off depending on the button state (0 or 1)
  }
});

function unexportOnClose() { //function to run when exiting program
  LED.writeSync(0); // Turn LED off
  LED.unexport(); // Unexport LED GPIO to free resources
  pushButton.unexport(); // Unexport Button GPIO to free resources
};

process.on('SIGINT', unexportOnClose); //function to run when user closes using ctrl+c
