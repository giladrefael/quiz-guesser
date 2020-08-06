

def fill_prob(answers):
    total = sum(answers.values())
    return {k: v / total for k, v in answers.items()}

def print_dict(d):
    to_print = {k:round(v,3) for k,v in d.items()}
    for k, v in to_print.items():
        print(k, v)

def get_input():
    print(">", end=' ')
    key = input()
    
    if key == 'q':
        print("Quiz finished -a good luck!")
        exit()
    elif key in 'a b c d'.split():
        return key
    else:
        return None

def get_all_min(d):
    min_key = min(d, key=d.get)
    return {k:v for k, v in d.items() if d[k] == d[min_key]}

def decide(prob, last_key):
    min_dict = get_all_min(prob)
    if last_key in min_dict.keys() and len(min_dict) > 1:
        del min_dict[last_key]

    if 'b' in min_dict.keys():
        answer = 'b'
    elif 'c' in min_dict.keys():
        answer = 'c'
    else:
        answer = list(min_dict.keys())[0]

    return answer

if __name__ == "__main__":
    answers = {'a':0,'b':0,'c':0,'d':0} 
    print("Quiz guesser - press q to quit")
    while True:
        key = get_input()
        if key:    
            answers[key] +=1
        else:
            continue

        prob = fill_prob(answers)
        print_dict(prob)
        
        answer = decide(prob, key)

        print("----------------")
        print(f"GUESS THIS -> {answer}")
        print("----------------\n")
    