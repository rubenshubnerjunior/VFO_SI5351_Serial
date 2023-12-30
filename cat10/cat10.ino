

#include <Wire.h>                          // Comunicacao I2C com o SI5351
#include "si5351.h"                        // Si5351 library
#include <SoftwareSerial.h>
#include <LiquidCrystal_I2C.h>             // LCD library


static const uint32_t bandStart = 3000000;     // Inicio da banda em HF (HZ)
static const uint32_t bandEnd =   30000000;    // Fim da banda HF (HZ)
static const uint32_t pll_min =   600000000;     //Frequencia minima do PLL (HZ)
static const uint32_t pll_max =   900000000;     //Frequencia maxima do PLL (HZ)

uint32_t pll_freq;
int multiple; // Multiplicador deve ser multiplo par da freq (freq * multiple = pll_freq)
volatile uint32_t oldfreq = 0;
volatile uint32_t freq = 7000000 ;

const int lcdColumns = 16;
const int lcdRows = 2;

Si5351 si5351;

LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);

//================Leitura da porta serial=========================

void leSerial()
{
  if (Serial.available())
  {
    String command = Serial.readString();
    Serial.print("Info da Serial:");
    Serial.println(command);
    command.toUpperCase();

    if (command.startsWith("FREQ"))
    {
      String arg = command.substring(command.indexOf(',') + 1); //(Mensagem do Hardware SDR ex:  FREQ,7000000)
      freq = arg.toInt();
      Serial.println((long int)freq);
    }
  }
}


//===========Ajusta valor da frequencia do  PLL e multiplicador=============
void GetPLLFreq() {

  uint32_t f_pll_freq;

  for (int i = 10; i <= 200; i = i + 2) {
    f_pll_freq = freq * i;
    if (f_pll_freq >= pll_min) {
      if (f_pll_freq <= pll_max) {
        if (f_pll_freq == floor(f_pll_freq)) {
          pll_freq = f_pll_freq;
          multiple = pll_freq / freq;
          break;
        }
      }
    }
  }

  Serial.println("----------------------------------------");
  Serial.print("Freq:");
  Serial.println(freq);

  Serial.print("Mult:");
  Serial.println(multiple);

  Serial.print("PLL:");
  Serial.println(pll_freq);

  showDisplay();

}
//==================Mostrar no Display===============
void showDisplay()
{
  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("                "); // Apaga a linha superior
  lcd.setCursor(0, 0);
  lcd.print(freq / 1000); // frequencia em KHZ
  lcd.setCursor(6, 0);
  lcd.print("Khz");
  lcd.setCursor(11, 0);
  lcd.print("OUT");


  lcd.setCursor(0, 1);
  lcd.print("                "); // Apaga a linha inferior
  lcd.setCursor(0, 1);
  lcd.print("PLL:");
  lcd.setCursor(4, 1);
  lcd.print(pll_freq / 1000); // frequencia em KHZ
  lcd.setCursor(11, 1);
  lcd.print("M:");
  lcd.setCursor(13, 1);
  lcd.print(multiple);

}

//================Ajusta a frequencia do modulo SI5351===========================
void SendFrequency()
{

  GetPLLFreq(); //obtem o valor da frequencia do PLL e do multiplicador par

  si5351.set_pll(pll_freq * 100ULL , SI5351_PLLA); //*100ULL para converter em 0.01 HZ

  si5351.set_freq_manual(freq * 100ULL, pll_freq * 100ULL, SI5351_CLK0); // *100ULL para converter HZ em 0.01 HZ
  si5351.set_freq_manual(freq * 100ULL, pll_freq * 100ULL, SI5351_CLK1); // *100ULL para converter HZ em 0.01 HZ

  si5351.set_phase(SI5351_CLK0, 0);         //Clock com 0º defasado
  si5351.set_phase(SI5351_CLK1, multiple); //Clock com 90º defasado

  si5351.pll_reset(SI5351_PLLA);
}

//=================================setup()======================
void setup() {

  Serial.begin(115200);
  lcd.init();
  lcd.backlight();

  if (si5351.init(SI5351_CRYSTAL_LOAD_8PF, 0, 0)) // Cristal 25 MHZ
  {
    Serial.println("SI5351 encontrado");
  }
  else
  {
    Serial.println("SI5351 Nao encontrado");
  }

  si5351.output_enable(SI5351_CLK0, 1);
  si5351.output_enable(SI5351_CLK1, 1);

  si5351.drive_strength(SI5351_CLK0, SI5351_DRIVE_2MA);
  si5351.drive_strength(SI5351_CLK1, SI5351_DRIVE_2MA);

  si5351.update_status();

}
//=============================loop()=================
void loop() {

  leSerial();

  if (freq != oldfreq)
  {
    if (freq <= bandEnd && freq >= bandStart) // A frequencia esta dentro da banda (3MHZ a 30MHZ)
    {
      SendFrequency();
      oldfreq = freq;
    }
    else
    {
      Serial.println("Frequencia fora da faixa");
      Serial.println("Mantendo o valor anterior");
      freq = oldfreq;

    }


  }

  delay(1);

}
