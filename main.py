from program_functions import *

waiting_for_new_stock = True
while waiting_for_new_stock:
    in_stock = check_in_stock()
    if not in_stock:
        print('Antminer S19 Pro still unavailable...')
        sleep(60)
    else:
        waiting_for_new_stock = False

notify_of_new_stock(subject_line, message_body)
print(f'Check your E-Mail, Antminer S19 Pro now in stock.\n{bitmain_url}')
