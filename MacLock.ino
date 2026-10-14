int pinA = A2;
int pinB = A3;
String sonKonum = "";

void setup() {
  Serial.begin(9600);
  pinMode(pinA, INPUT_PULLUP);
  pinMode(pinB, INPUT_PULLUP);
}

void loop() {
  int durumA = digitalRead(pinA);
  int durumB = digitalRead(pinB);
  String anlikKonum = "";

  if (durumA == LOW) {
    anlikKonum = "ON1";
  } 
  else if (durumB == LOW) {
    anlikKonum = "ON2";
  } 
  else {
    anlikKonum = "OFF"; 
  }

  // Eğer konumda bir farklılık sezerse...
  if (anlikKonum != sonKonum) {
    
    // Şalterin mekanik geçişini bitirmesi için 0.2 saniye bekle
    delay(200); 
    
    // Geçiş bittikten sonra emin olmak için son durumu tekrar oku
    durumA = digitalRead(pinA);
    durumB = digitalRead(pinB);
    
    if (durumA == LOW) anlikKonum = "ON1";
    else if (durumB == LOW) anlikKonum = "ON2";
    else anlikKonum = "OFF";

    // Eğer o 0.2 saniye sonunda konum gerçekten kalıcı olarak değiştiyse yazdır
    if (anlikKonum != sonKonum) {
      Serial.println(anlikKonum);
      sonKonum = anlikKonum;
    }
  }
}