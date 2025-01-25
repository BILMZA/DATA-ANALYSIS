import time
import psutil
import pyodbc

# Connect to SQL Server
connection = pyodbc.connect('Driver={SQL Server};'
                             'Server=BILMZA\\SQLEXPRESS; '
                             'Database=SYSTEM_INFORMATION;'
                             'Trusted_Connection=yes;')

cursor = connection.cursor()

# Main loop to gather system performance data
while True:
    usage_of_cpu = psutil.cpu_percent()
    cpu_interrupt = psutil.cpu_stats().interrupts
    cpu_calls = psutil.cpu_stats().ctx_switches
    byte_sent = psutil.net_io_counters().bytes_sent
    byte_received = psutil.net_io_counters().bytes_recv
    memory_free = psutil.virtual_memory().available
    memory_usage = psutil.virtual_memory().percent
    memory_used = psutil.virtual_memory().used

    # Insert data into the Peformance table
    cursor.execute('insert into thenewperformance values (' 
                   + str(usage_of_cpu) + ', ' 
                   + str(cpu_interrupt) + ', ' 
                   + str(cpu_calls) + ', ' 
                   + str(byte_sent) + ', ' 
                   + str(byte_received) + ', ' 
                   + str(memory_free) + ', ' 
                   + str(memory_usage) + ', ' 
                   + str(memory_used) + ')')
    
    # Commit the transaction
    connection.commit()
    
    # Sleep for 5 seconds before repeating the process
    time.sleep(3)
