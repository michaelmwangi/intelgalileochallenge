
const int tempSense=A0;
float tempVal=0.0;

const int PEOPLEINPIN = 13;
const int PEOPLEOUTPIN = 12;
int TOTALPEOPLE =0;
bool GETINATTEMPT = false;
bool GETOUTATTEMPT = false;
bool OUT =false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
   pinMode(tempSense,INPUT);
   pinMode(PEOPLEINPIN,INPUT);
   pinMode(PEOPLEOUTPIN,INPUT);
   
}
void count_people(){
  if (digitalRead(PEOPLEINPIN) == HIGH)  {
    Serial.println("In");    
    if(GETOUTATTEMPT == true){
      if (TOTALPEOPLE ){
        TOTALPEOPLE =TOTALPEOPLE-1;
      }
      else{
        TOTALPEOPLE = 0;
      }
      GETOUTATTEMPT = false;
      GETINATTEMPT = false;
      OUT = true;
    }
    else{
    if (OUT == false)
	GETINATTEMPT= true;      
//     OUT = false;
    }
  }
  else if(digitalRead(PEOPLEOUTPIN) == HIGH){
    Serial.println("Out");
    
    if (GETINATTEMPT == true){
      TOTALPEOPLE +=1;
      GETINATTEMPT = false;
      GETOUTATTEMPT = false;
      OUT = true;
    }
    else{
      if (OUT == false)
	GETOUTATTEMPT= true;
      OUT = false;
    }
    
  }
}


void loop() {
  // put your main code here, to run repeatedly: 
 // float tempC = (5.0 * analogRead(TEMPPIN) * 100.0)/1024.0; 
 // Serial.println(tempC);
   count_people();
  tempVal=analogRead(tempSense)*0.48828125;
  Serial.print("People: ");
  Serial.println(TOTALPEOPLE);
  
  Serial.print("Temperature: ");
  Serial.println(tempVal);
  delay(100);
}

