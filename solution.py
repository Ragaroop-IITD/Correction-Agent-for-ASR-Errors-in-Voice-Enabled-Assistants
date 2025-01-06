import time
# from tqdm import tqdm
# from pprint import pprint
class Agent(object):
    def __init__(self, phoneme_table, vocabulary) -> None:
        self.phoneme_table = phoneme_table
        self.vocabulary = vocabulary
        self.best_state = ""
        self.best_cost = ""
        #convert phoneme table to a reverse phoneme table ; where value is list
        self.phoneme_table_r = {}
        self.time = None
        for key, value in self.phoneme_table.items():
            for v in value:
                if v in self.phoneme_table_r:
                    self.phoneme_table_r[v].append(key)
                else:
                    self.phoneme_table_r[v] = [key]
                    
    def asr_corrector(self, environment):
        start = time.time() 
        self.best_state = environment.init_state
        self.best_cost = environment.compute_cost(environment.init_state)
        init_state = self.best_state
        made_changes = True
        # print("Initial Changes")
        while made_changes:
            made_changes=self.get_phoneme_subs_a(environment)
            print("Initial Changes")
            print(self.best_state)
            
        # print("\n\nReplaced with.....")
        self.check_init_replace(environment,init_state)
        # print(self.best_state)
        
        self.append_front(environment)
        self.append_back(environment)
        self.time = time.time()-start

        print("\n\nbest")
        print(self.best_state,self.best_cost)
        print(time.time()-start)
        
    def check_init_replace(self,environment,init_state):
        words_init = init_state.split()
        words = self.best_state.split()
        for i in range(len(words)):
            if words[i] != words_init[i]:
                word = words_init[i]
                for k in range(len(word)-1):
                    p_check = word[k:k+2]
                    p_variants = self.get_phoneme_variants(p_check)
                    for p in p_variants:
                        word_new = word[:k] + p + word[k+2:]
                        new_state = ' '.join(words[:i] + [word_new] + words[i+1:])
                        cost = environment.compute_cost(new_state)
                        if cost < self.best_cost:
                            self.best_cost = cost
                            self.best_state = new_state
                            words[i]=word_new
                            
        
    def append_front(self, environment):
        init_state = self.best_state
        init_cost = self.best_cost
        for word in self.vocabulary:
            new_state = word + ' ' + init_state
            cost = environment.compute_cost(new_state)
            if cost < self.best_cost:
                self.best_cost = cost
                self.best_state = new_state
        # print("Appending Front Done")

    def append_back(self, environment):
        init_state = self.best_state
        init_cost = self.best_cost
        for word in self.vocabulary:
            new_state = init_state + ' ' + word
            cost = environment.compute_cost(new_state)
            if cost < self.best_cost:
                self.best_cost = cost
                self.best_state = new_state
        # print("Appending Back Done")

                
    def get_phoneme_subs_a(self, environment):
        made_changes = False
        best_cost = self.best_cost
        current_state = self.best_state
        words = current_state.split()
        for i in range(len(words)):
            word = words[i]
            for k in range(len(word)-1): #phonome length -1
                p_check = word[k:k+2] #phoneme length
                p_variants = self.get_phoneme_variants(p_check)
                for variant in p_variants:
                    new_state = ' '.join(words[:i] + [word[:k] + variant + word[k+2:]] + words[i+1:])
                    cost = environment.compute_cost(new_state)
                    if cost < best_cost:
                        best_cost = cost
                        self.best_state = new_state
                        words[i]=word[:k] + variant + word[k+2:]
                        made_changes = True
            # pprint(words[i])
        self.best_cost = best_cost
        return made_changes
        
    def get_phoneme_variants(self,word):
        """
        Generate variants of a word by applying all possible phoneme replacements.
        """
        answer = [word]
        for phoneme,replacemnts in self.phoneme_table_r.items():
            if phoneme in word:
                if len(phoneme) == 1:
                    for i in range(len(word)):
                        if word[i] == phoneme:
                            for r in replacemnts:
                                answer.append(word[:i] + r + word[i+1:])
                else:
                    for i in range(len(word)-1):
                        if word[i:i+2] == phoneme:
                            for r in replacemnts:
                                answer.append(word[:i] + r + word[i+2:])
        return answer   
    
