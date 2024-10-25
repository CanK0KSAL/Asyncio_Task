import asyncio
import random

waiting_time = [1, 3, 10]

async def get_the_visa():
    print('1. Arrive to Embassy')  
    await asyncio.sleep(1)
    print('2. Fill the Visa form') 
    await asyncio.sleep(1)
    print('3. Pay the charge') 
    print('Waiting for the message from Embassy...')
    await asyncio.sleep(random.choice(waiting_time))  

    print('-> [EVENT] Notification from Embassy - Visa is ready!')  
    await asyncio.sleep(1)
    print('4. Arrive to Embassy')   
    await asyncio.sleep(1)
    print('5. Receive the VISA')  
    
async def find_accomodation():
    print('Post on Facebook that you are looking for accommodation') 
    print('Waiting for the message from friends...')
    await asyncio.sleep(random.choice(waiting_time))  
    
    print('-> [EVENT] Message from friend - I have a room for you')  
    await asyncio.sleep(1)
    print('[ACCOMMODATION][STEP 2] - Accept the offer')  
    await asyncio.sleep(1)
    print('[ACCOMMODATION][STEP 3] - Pay the deposit for the room') 
    

async def enroll_for_the_semester():
    print('Send email to school with your documents')  
    print('Waiting for the message from school...')
    await asyncio.sleep(random.choice(waiting_time))  
    
    print('-> [EVENT] Message from school - Document accepted; enrollment payment is due.') 
    await asyncio.sleep(1)
    print('[ENROLLMENT][STEP 2] - Confirm enrollment')  
    await asyncio.sleep(1)
    print('[ENROLLMENT][STEP 3] - Pay enrollment fees')  
    

async def buy_new_laptop():
    print('Go to the bank to request a loan') 
    print('Waiting while the bank checks your credit score...')
    await asyncio.sleep(random.choice(waiting_time)) 

    print('-> [EVENT] Message from bank - Credit request approved')
    await asyncio.sleep(1)
    print('[BANK][STEP 2] - Accept loan offer') 
    await asyncio.sleep(1)
    print('[BANK][STEP 3] - Take the loan and buy your new laptop') 
    
    
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
