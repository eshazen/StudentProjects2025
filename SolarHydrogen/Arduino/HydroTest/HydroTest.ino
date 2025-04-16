//
// Initial hydrogen generator control panel
//
// Use keypad to control PWM and thus hydrolysis current
// 

#include <TimerOne.h>
#include <ctype.h>
#include <LiquidCrystal.h>

static const int pwmPin = 9;	// PWM pin (must be 9 or 10 for TimerOne library!)

// LCD display wiring
const int rs = 8, en = 12, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// global variables
static int pwm = 1;		// current PWM setting
static int last_key = 0;	// last reading from keypad ADC

// expected analog values for pins on keypad
// keys               down up   left right  sel
static int keyz[] = { 253, 98,  405, 0,     636};
#define NKEYZ (sizeof(keyz)/sizeof(keyz[0]))
#define ABS(x) (((x)<0)?(-(x)):(x))

// set the PWM to p where p is 1..2..3 etc and display
// (actual value is 13x the passed value due to behavior of timer 1 at 100kHz)
void setPWM( int p) {
  if( p < 1)
    p = 1;
  Timer1.pwm( pwmPin, p*13);
  lcd.setCursor(0, 1);
  lcd.print("PWM: ");
  lcd.print( p);
  lcd.print("  ");
}

// convert ADC value from keypad to key hit (0 for none, 1 = down etc)
int key_hit( int a) {
  if( a > 1010)			// max reading = no key pressed
    return 0;
  for( int i=0; i<NKEYZ; i++) {	// check against possible key values
    if( ABS(a-keyz[i]) < 5)	// allow for 5 counts error
      return i+1;
  }
  return 0;
}

// -------------------- Arduino setup ----------
void setup() {
  Timer1.initialize(10);  // Start the PWM timer:  10 us = 100 kHz
  setPWM( 1);		  // set to minimum width
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Hydrogener V0.1");
}

// -------------------- Arduino main loop --------------------
void loop() {

  // check for key press
  int key = key_hit(analogRead( 0));
  if( key && !last_key) {
    switch( key) {
    case 1:			// down
      if( pwm > 1)
	--pwm;
      setPWM( pwm);
      break;
    case 2:			// up
      if( pwm < 50)
	++pwm;
      setPWM( pwm);
      break;
    case 3:			// left
      break;
    case 4:			// right
      break;
    case 5:			// sel
      break;
    default:
      ;
    }
  }

  last_key = key;
  delay(100);
}
