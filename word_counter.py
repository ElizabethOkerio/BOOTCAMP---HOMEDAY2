def words(sentence):
   sentence_dict = {}
   sentence_list = sentence.split()
 
   for word in sentence_list:
       if word.isdigit():
           word = int(word)
       if word in sentence_dict:
           sentence_dict[word] += 1
       else:
           sentence_dict[word] = 1
   return sentence_dict
