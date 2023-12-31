
## Objetivo gerar frequência em quadratura para testes de SDR:

#### Comanda o modulo SI5351 com o arduino através do protocolo I2C.
#### O arduino nano recebe via porta serial a  String-->   *freq,3000000*
#### Após a virgula temos que informar a frequência desejada em Hz.
#### A saida do módulo termos dois clocks em quadratura:
- CLK0-->0º 
- CLK1--> 90º.
#### A banda foi limitada entre 3 Mhz a 30 Mhz.
#### A porta Serial está configurada para 115200 bauds.
#### Pode-se gerar a String de comando com terminais, por exemplo:
- Monitor Serial do arduino.
- Programa Termite da CompuPhase.
- HDSDR via Omnirig, neste caso a seleção de frequência no programa HDSDR ajusta a frequência do VFO automaticamente.
## Uso do terminal Monitor Serial do Arduino.
-- Seguir as configurações conforme a imagem:

## Uso do terminal Termite:
-- Seguir as configurações conforme a imagem:

## Uso do HDSDR para comandar a frequência do VFO.
- Instalar o HDSDR.
- Instalar o Omni-Rig V.2.
- Copiar o arquivo MYSDR.ini para a pasta %APPDATA%\Afreet\Rigs
- Ajustar o Omnirig e o HDSDR conforme a imagem.

