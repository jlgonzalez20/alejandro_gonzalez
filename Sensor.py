import serial
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

PORT = "COM4"   # ⚠️ Ajusta al puerto correcto
BAUDRATE = 9600

HEADER = b"\xAA"
COMMAND = b"\xC0"
TAIL = b"\xAB"

# Archivo donde guardaremos los datos
FILE_NAME = "mediciones.txt"

# Listas para graficar
timestamps = []
pm25_values = []
pm10_values = []
   
def read_sds011(port=PORT, baudrate=BAUDRATE):
    ser = serial.Serial(port, baudrate, timeout=2)
    byte, prev = b"\x00", b"\x00"

    # Configuración del gráfico
    plt.ion()
    fig, ax = plt.subplots()
    line1, = ax.plot([], [], label="PM2.5 (µg/m³)")
    line2, = ax.plot([], [], label="PM10 (µg/m³)")
    ax.legend()
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Concentración (µg/m³)")

    # Formato de fecha en eje X
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())

    while True:
        prev = byte
        byte = ser.read(1)

        if prev == HEADER and byte == COMMAND:
            packet = ser.read(8)

            if len(packet) == 8:
                pm25 = (packet[1] << 8 | packet[0]) / 10.0
                pm10 = (packet[3] << 8 | packet[2]) / 10.0
                sensor_id = f"{packet[4]:02X}{packet[5]:02X}"
                checksum = packet[6]
                calc_checksum = (sum(packet[0:6]) & 0xFF)
                tail = packet[7]

                if checksum == calc_checksum and tail == 0xAB:
                    now = datetime.now()
                    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"✅ {now_str} | PM2.5: {pm25:.1f} µg/m³ | PM10: {pm10:.1f} µg/m³ | ID: {sensor_id}")

                    # Guardar en archivo
                    with open(FILE_NAME, "a") as f:
                        f.write(f"{now_str}, PM2.5={pm25:.1f}, PM10={pm10:.1f}, ID={sensor_id}\n")

                    # Agregar a listas
                    timestamps.append(now)
                    pm25_values.append(pm25)
                    pm10_values.append(pm10)

                    # Actualizar gráfico
                    line1.set_xdata(timestamps)
                    line1.set_ydata(pm25_values)
                    line2.set_xdata(timestamps)
                    line2.set_ydata(pm10_values)

                    ax.relim()
                    ax.autoscale_view()
                    plt.xticks(rotation=45, ha="right")
                    plt.tight_layout()
                    plt.pause(0.1)

        time.sleep(0.1)


if __name__ == "__main__":
    try:
        print("📡 Iniciando lectura y guardado de datos del SDS011...")
        read_sds011()
    except KeyboardInterrupt:
        print("\n👋 Lectura detenida por el usuario")
        plt.ioff()
        plt.show()
