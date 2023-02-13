import matplotlib.pyplot as plt
import serial 


x = []

Xacc= []
Yacc= []
Zacc = []

P= []
Alt = []

Pitch= []
Yaw= []
Roll = []



cnt = 0

arduino = serial.Serial(port='/dev/cu.usbserial-141120', baudrate=115200, timeout=1)

def parseFrame():
    dataFrame = str(arduino.readline())
    splitFrame = dataFrame.split(",")
    #print(arduino.readline())
    print(dataFrame)
    if len(splitFrame)>3:
        print(int(splitFrame[9]))
    return splitFrame



f, axis = plt.subplots(2, 2)
plt.ion()



axis[0, 0].set_title('Acceleration')
axis[0, 0].set_xlabel('seconds', fontsize = 1)
axis[0, 0].set_ylabel('g')

while True:
    data = parseFrame()

    if len(data)>3:

        #timestamp,Xacc,Yazz,Zacc,Pressure,Altitude,Pitch,Yaw,Roll
        x.append(int(data[1]))
        Xacc.append(int(data[2]))
        Yacc.append(int(data[3]))
        Zacc.append(int(data[4]))
        P.append(int(data[5]))
        Alt.append(int(data[6]))
        Pitch.append(int(data[7]))
        Yaw.append(int(data[8]))
        Roll.append(int(data[9]))

        #print(data)


        axis[0,0].plot(x, Xacc, color = 'r', linestyle = 'solid', marker = '',label = "X axis")
        axis[0,0].plot(x, Yacc, color = 'g', linestyle = 'solid', marker = '',label = "Y axis")
        axis[0,0].plot(x, Zacc, color = 'b', linestyle = 'solid', marker = '',label = "Z axis")

        axis[0,1].plot(x, Alt, color = 'r', linestyle = 'solid', marker = '',label = "Altitude")
       
        axis[1,0].plot(x, Pitch, color = 'r', linestyle = 'solid', marker = '',label = "Pitch")
        axis[1,0].plot(x, Yaw, color = 'g', linestyle = 'solid', marker = '',label = "Yaw")
        axis[1,0].plot(x, Roll, color = 'b', linestyle = 'solid', marker = '',label = "Roll")


       
        if cnt == 0:
            axis[0, 0].legend()
            axis[0, 1].legend()
            axis[1, 0].legend()
            cnt+=1
        

        plt.show()
        plt.pause(0.05)
   
