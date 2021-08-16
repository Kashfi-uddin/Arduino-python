
int photosensor = 0;

void setup()
{
  pinMode(A0, INPUT);
  Serial.begin(9600);

  pinMode(11, OUTPUT);
}

void loop()
{
  photosensor = analogRead(A0);
  Serial.println(photosensor);
  analogWrite(11,map(photosensor,0,1023,0,255));
  delay(500); // Delay a little bit to improve simulation performance
}
