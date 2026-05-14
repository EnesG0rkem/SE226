int LED1pin = 43;
int LED2pin = 44;
int LED3pin = 45;
int LED4pin = 46;

byte LED1State = LOW;
byte LED2State = LOW;
byte LED3State = LOW;
byte LED4State = LOW;

int BUTTON1pin = 38;
int BUTTON2pin = 39;
int BUTTON3pin = 40;
int BUTTON4pin = 41;

byte BUTTON1lastState = LOW;
byte BUTTON2lastState = LOW;
byte BUTTON3lastState = LOW;
byte BUTTON4lastState = LOW;


void setup(){
pinMode(LED1pin,OUTPUT);
pinMode(LED2pin,OUTPUT);
pinMode(LED3pin,OUTPUT);
pinMode(LED4pin,OUTPUT);  

pinMode(BUTTON1pin, INPUT);
pinMode(BUTTON2pin, INPUT);
pinMode(BUTTON3pin, INPUT);
pinMode(BUTTON4pin, INPUT);
}

void loop(){
    byte button1State = digitalRead(BUTTON1pin);
  if(button1State == HIGH){
    LED1State = !LED1State;
    digitalWrite(LED1pin, LED1State);
  }

    byte button2State = digitalRead(BUTTON2pin);
  if(button2State == HIGH){
    LED2State = !LED2State;
    digitalWrite(LED2pin, LED2State);
  }

    byte button3State = digitalRead(BUTTON3pin);
  if(button3State == HIGH){
    LED3State = !LED3State;
    digitalWrite(LED3pin, LED3State);
  }

    byte button4State = digitalRead(BUTTON4pin);
  if(button4State == HIGH){
    LED4State = !LED4State;
    digitalWrite(LED4pin, LED2State);
  }
/*digitalWrite(LED1pin,HIGH);
delay(100);
digitalWrite(LED1pin,LOW);
delay(100);
digitalWrite(LED2pin,HIGH);
delay(100);
digitalWrite(LED2pin,LOW);
delay(100);
digitalWrite(LED3pin,HIGH);
delay(100);
digitalWrite(LED3pin,LOW);
delay(100);
digitalWrite(LED4pin,HIGH);
delay(100);
digitalWrite(LED4pin,LOW);
delay(100); */
}
