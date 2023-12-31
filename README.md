
## Objetivo gerar sinais (VFO) em quadratura para testes de SDR:

#### Comanda o modulo SI5351 com o arduino através do protocolo I2C.
#### O arduino nano recebe via porta serial a String no formato:   *freq,3000000*
#### Após a virgula informar a frequência desejada em Hz.
#### A saida do módulo termos dois clocks em quadratura:
- CLK0-->0º 
- CLK1--> 90º.
#### A banda foi limitada entre 3 Mhz a 30 Mhz.
#### A porta Serial está configurada para 115200 bauds e terminada com NL.
#### Pode-se gerar a String de comando com terminais, por exemplo:
- Monitor Serial do arduino.
- Programa Termite da CompuPhase.
- HDSDR via Omnirig, neste caso mudando a frequência no programa HDSDR a frequência do VFO acompanha automaticamente.
## Uso do terminal Monitor Serial do Arduino.
- Veja no gerenciador de dispositivos qual a porta *Com* utilizada pelo arduino.
- Seguir as configurações conforme a imagem:
- ![alt text](https://github.com/rubenshubnerjunior/VFO_SI5351_Serial/blob/main/Fotos/Serial_Monitor.jpg)
## Uso do terminal Termite:
- Veja no gerenciador de dispositivos qual a porta *Com* utilizada pelo arduino.
- Seguir as configurações conforme a imagem:
- ![alt text](https://github.com/rubenshubnerjunior/VFO_SI5351_Serial/blob/main/Fotos/termite.jpg)

## Uso do HDSDR para comandar a frequência do VFO.
- Instalar o HDSDR.
- Instalar o Omni-Rig V.2.
- Copiar o arquivo MYSDR.ini para a pasta %APPDATA%\Afreet\Rigs
-  Veja no gerenciador de dispositivos qual a porta *Com* utilizada pelo arduino.
-  Na aba options do HDSDR ajustar o HDSDR e Omni-Rig conforme imagem abaixo:
-  ![alt text](https://github.com/rubenshubnerjunior/VFO_SI5351_Serial/blob/main/Fotos/HDSDR_1.jpg)
## Montagem no protoboard para testes.
-  ![alt text](https://github.com/rubenshubnerjunior/VFO_SI5351_Serial/blob/main/Fotos/protoboard.jpg)
  ## Testes.
-  ![alt text](https://github.com/rubenshubnerjunior/VFO_SI5351_Serial/blob/main/Fotos/geral.jpg)

## Sobre o Sketch usado no arduino
- A principal biblioteca si5351.h da etherkit:
- https://github.com/etherkit/Si5351Arduino


