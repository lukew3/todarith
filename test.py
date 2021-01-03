import tracemalloc, random, time

def auto_generate():
    tracemalloc.start()
    while 0 == 0:
        gen_id = random.randint(0, 100)
        try:
            print("Before: " + str(tracemalloc.get_traced_memory()[0]))
            p, a, s = generate_problem(gen_id)
            print("After: " + str(tracemalloc.get_traced_memory()[0]))
        except Exception as e:
            pass
        time.sleep(0.2)
        current, peak = tracemalloc.get_traced_memory()

def generate_problem(gen_id):
    if prob == "1+2":
        prob = "1+1"
    else:
        prob = "1 + 2"
        
    ans = "3"
    generator_name = "Addition"
    return prob, ans, generator_name

auto_generate()
