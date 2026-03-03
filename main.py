from robotics import *
from time import *

# Ham nang thanh chan
def nang_thanh():
    servo_write(S1, 0)
    servo_write(S2, 0)

# Ham ha thanh chan
def ha_thanh():
    servo_write(S1, 90)
    servo_write(S2, 90)

# Ham thuc hien day hat giong
def day_hat_giong():
    ha_thanh()
    sleep(0.5)
    # Dung Encoder day vao 30cm, toc do 60
    robot.move_distance(30, 60)
    sleep(0.3)
    # Lui lai 15cm
    robot.move_distance(-15, 50)
    nang_thanh()

# Ham Auto khi nhan nut Boot
def chay_tu_dong():
    display.show("RUN")
    # Tien den cho hat giong 60cm
    robot.move_distance(60, 50)
    # Thuc hien chuoi day hat
    day_hat_giong()
    display.show("WAIT")

# --- BAT DAU VONG LAP CHINH ---
display.show("ORC")
nang_thanh()

while True:
    # Nhan nut Boot tren Hub de chay nhanh nhiem vu day
    if button_is_pressed(BOOT):
        chay_tu_dong()

    # Dieu khien di chuyen bang nut bam Gamepad
    if gamepad.is_pressed(BTN_UP):
        robot.forward(50)
    elif gamepad.is_pressed(BTN_DOWN):
        robot.backward(50)
    elif gamepad.is_pressed(BTN_LEFT):
        robot.m_side_step(-50)
    elif gamepad.is_pressed(BTN_RIGHT):
        robot.m_side_step(50)
    else:
        # Neu khong bam nut thi dung Joystick
        robot.drive_mecanum(gamepad.get_joystick(JOY_LY), gamepad.get_joystick(JOY_LX), gamepad.get_joystick(JOY_RX))

    # Nut phu dieu khien thanh chan
    if gamepad.is_pressed(BTN_L1):
        ha_thanh()
    if gamepad.is_pressed(BTN_R1):
        nang_thanh()

    sleep(0.01)
