import time
from gas_detection import GasDetection
import Temperatur
import random
import api 
import SoundandEmail

def main():
    """Handle example."""

    print('Calibrating ...')
    detection = GasDetection()
    
    counter =  1 
    try:
        while True:
            ppm = detection.percentage()
            temp = float(Temperatur.aktuelleTemperatur())
            
#Sensorwerte
            #print('CO: {} ppm'.format(ppm[detection.CO_GAS])
            #print('LPG: {} ppm'.format(ppm[detection.LPG_GAS]))
            #print('SMOKE: {} ppm\n'.format(ppm[detection.SMOKE_GAS]))
            print(f'Tepmperatur: {temp} Grad Celsius')
            
#simulierte Werte
            L = random.randint(2600,2700)
            C = random.randint(4000,4300)
            S = random.randint(950,1050)
                  
            LPG = (temp/L)*(temp/22)**20 
            CO = (temp/C)*(temp/22)**20
            SMOKE = (temp/S)*(temp/22)**20

            print(f'LPG: {LPG} ppm') 
            print(f'CO: {CO} ppm')
            print(f'Smoke: {SMOKE} ppm \n')
            
            time.sleep(1)
            api.adding_data(device_id=1,temp=temp, lpg = LPG, co = CO, smoke = SMOKE)
            
            if SMOKE > 10 and counter == 1:
                counter = 0
                SoundandEmail.firealarm()
                SoundandEmail.sendmail()
                api.lichtan()
            else:
                pass
            
                

    except KeyboardInterrupt:
        print('\nAborted by user!')
        api.lichtaus()
        SoundandEmail.pygame.mixer.quit()

if __name__ == '__main__':
    main()