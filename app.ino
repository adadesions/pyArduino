#define LED2 2
#define LED4 4
#define LED7 7

void setup() {
    pinMode(LED2, OUTPUT);
    pinMode(LED4, OUTPUT);
    pinMode(LED7, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        String listener = "";
        listener = Serial.readString();
        int LED[3] = {LED2, LED4, LED7};
        int led_index = listener[0]-'0';
        if (listener[1] == '1') {
            digitalWrite(LED[led_index], HIGH);
        }
        else if (listener[1] == '0') {
            digitalWrite(LED[led_index], LOW);
        }
    }
}