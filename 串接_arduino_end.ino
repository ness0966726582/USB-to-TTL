void setup(){
  Serial.begin(9600);
}
 
void loop(){ 
  //Serial.print("Moisture Sensor Value:");
  Serial.print(analogRead(A0));
  Serial.print(",");    
  Serial.println(analogRead(A0));  
  delay(500);
}
