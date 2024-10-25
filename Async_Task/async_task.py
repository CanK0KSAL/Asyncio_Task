import asyncio
import random

waiting_time = [1, 3, 10]

async def get_the_visa():
    print('1. Arrive to Embassy')  # Step 1
    await asyncio.sleep(1)
    print('2. Fill the Visa form')  # Step 2
    await asyncio.sleep(1)
    print('3. Pay the charge')  # Step 3
    print('Waiting for the message from Embassy...')
    await asyncio.sleep(random.choice(waiting_time))  # Waiting for event

    print('-> [EVENT] Notification from Embassy - Visa is ready!')  # Event
    await asyncio.sleep(1)
    print('4. Arrive to Embassy')  # Step 4  
    await asyncio.sleep(1)
    print('5. Receive the VISA')  # Step 5
    
async def find_accomodation():
    print('Post on Facebook that you are looking for accommodation')  # Step 1
    print('Waiting for the message from friends...')
    await asyncio.sleep(random.choice(waiting_time))  # Waiting for event
    
    print('-> [EVENT] Message from friend - I have a room for you')  # Event
    await asyncio.sleep(1)
    print('[ACCOMMODATION][STEP 2] - Accept the offer')  # Step 2
    await asyncio.sleep(1)
    print('[ACCOMMODATION][STEP 3] - Pay the deposit for the room')  # Step 3
    

async def enroll_for_the_semester():
    print('Send email to school with your documents')  # Step 1
    print('Waiting for the message from school...')
    await asyncio.sleep(random.choice(waiting_time))  # Waiting for event

    print('-> [EVENT] Message from school - Document accepted; enrollment payment is due.')  # Event
    await asyncio.sleep(1)
    print('[ENROLLMENT][STEP 2] - Confirm enrollment')  # Step 2
    await asyncio.sleep(1)
    print('[ENROLLMENT][STEP 3] - Pay enrollment fees')  # Step 3
    

async def buy_new_laptop():
    print('Go to the bank to request a loan')  # Step 1
    print('Waiting while the bank checks your credit score...')
    await asyncio.sleep(random.choice(waiting_time))  # Waiting for event

    print('-> [EVENT] Message from bank - Credit request approved')  # Event
    await asyncio.sleep(1)
    print('[BANK][STEP 2] - Accept loan offer')  # Step 2
    await asyncio.sleep(1)
    print('[BANK][STEP 3] - Take the loan and buy your new laptop')  # Step 3
    
    
async def main():
    # Run tasks concurrently using gather
    await asyncio.gather(
        get_the_visa(),
        find_accomodation(),
        enroll_for_the_semester(),
        buy_new_laptop()
    )

# Run the event loop
asyncio.run(main())
