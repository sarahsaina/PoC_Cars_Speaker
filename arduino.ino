int tempVal;      //temperature sensor readings
float volts;      //voltage 
float temp;       //real temperature
int lumi;         //brightness

void setup() {
  Serial.begin(9600); 
}

void loop() {
  tempVal = analogRead(15);     // read analog input pin 15
  lumi = analogRead(2);         // read analog input pin 2
  volts = tempVal / 1023.0;
  temp = (volts - 0.5) * 100;
  
  Serial.print(temp, DEC);
  Serial.print(",");
  Serial.print(lumi, DEC);      // prints the value read, decimal values only
  
  delay(1000);              // wait for 1s

}
