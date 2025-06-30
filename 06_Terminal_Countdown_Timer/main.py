
import time 

time_remaining = int(input("Enter the time in seconds: "))

while time_remaining > 0:
    hours = time_remaining // 3600
    minutes = (time_remaining % 3600) // 60
    seconds = time_remaining % 60
    print(" " * 40, end='\r')
    print( f"{hours : 02}:{minutes : 02}:{seconds : <02} ", end='\r', flush=True)
    time.sleep(1)
    
                
    if time_remaining == 10:
        print("⚠️ Hurry up! Only 10 seconds left!",end='\r', flush=True)
        time.sleep(1)
        time_remaining -= 2
        continue

    time_remaining -= 1



print( "⏰ Time's up!")
