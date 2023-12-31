
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
- Seguir as configurações conforme a imagem:

## Uso do terminal Termite:
- Seguir as configurações conforme a imagem:
- ![alt text](path/to/file)

## Uso do HDSDR para comandar a frequência do VFO.
- Instalar o HDSDR.
- Instalar o Omni-Rig V.2.
- Copiar o arquivo MYSDR.ini para a pasta %APPDATA%\Afreet\Rigs
- Ajustar o Omnirig e o HDSDR conforme a imagem.

