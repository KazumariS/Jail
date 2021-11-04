import time, rotatescreen as rs 
pd = rs.get_primary_display()
posisi = [90, 180, 270, 0]
while True:
    for x in posisi:
        pd.rotate_to(x)
        time.sleep(0.5)
