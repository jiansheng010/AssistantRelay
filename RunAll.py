import threading
import AssistantRelayProg
import KeyPressProg
import time


def keylogger_thread():
    print('Starting key logger...')
    KeyPressProg.run_keypress()
    print('Key Logger stopped.')


def assistant_thread():
    print('Starting program...')
    ret_code = AssistantRelayProg.run_program()
    print("Program finished with exit code " + str(ret_code))


if __name__ == '__main__':
    t1 = threading.Thread(target=assistant_thread())
    t2 = threading.Thread(target=keylogger_thread())
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Completed.")


