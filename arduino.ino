int tempVal;      //temperature sensor readings
float volts;      //voltage 
float temp;       //real temperature
int lumi;         //light sensor

void setup() {
  Serial.begin(9600); 
}

void loop() {
  tempVal = analogRead(15);     // read analog input pin 15
  lumi = analogRead(2);         // read analog input pin 2
  volts = tempVal * (3300/1024); // this formula converts the number 0-1023 from the ADC into 0-3300mV
  temp = (volts - 500) / 100; // this formula converts the voltage into a temperature in °C
  Serial.print(temp, DEC);
  Serial.print(",");
  Serial.print(lumi, DEC); // prints the value read, decimal values only
  Serial.print("\n");       
  delay(1000);            // wait for 1s
}
