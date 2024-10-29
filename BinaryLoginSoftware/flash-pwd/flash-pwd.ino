#include "DigiKeyboard.h"  //DigiKeyboard library

void setup() {
  //None
}

void loop() {
  //Send null keystroke to initialize
  DigiKeyboard.sendKeyStroke(0);
  
  //delay
  DigiKeyboard.delay(1000);

  //Type string and press Enter
  DigiKeyboard.println("cmpenis#1");

  //Stop program
  for(;;);
}
