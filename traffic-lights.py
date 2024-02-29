const int led_green = 23; // Define the pin for the yellow LED
const int led_yellow = 22; // Define the pin for the red LED
const int led_red = 21; // Define the pin for the green LED

void setup() {
  pinMode(led_yellow, OUTPUT); // Set the yellow LED pin as an output
  pinMode(led_red, OUTPUT); // Set the red LED pin as an output
  pinMode(led_green, OUTPUT); // Set the green LED pin as an output
}

void loop() {
  digitalWrite(led_green, HIGH); // Turn on the green LED
  digitalWrite(led_yellow, LOW);
  digitalWrite(led_red, LOW);
  delay(2000); // Wait for 1 second
  
  digitalWrite(led_green, LOW); 
  digitalWrite(led_yellow, HIGH); // Turn on the yellow LED
  digitalWrite(led_red, LOW); 
  delay(2000);
  
  digitalWrite(led_green, LOW); 
  digitalWrite(led_yellow, LOW);
  digitalWrite(led_red, HIGH); // Turn on the red LED
  delay(1000);
  digitalWrite(led_yellow, HIGH);
  delay(2000);
}
