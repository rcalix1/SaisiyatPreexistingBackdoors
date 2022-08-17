
f_7090 = open("ForTrainingSubwords7090.csv", 'r')


labelled_train_dict = {}

for line in f_7090.readlines():
    
    temp = line.split('\t')

    recall    = temp[1].replace(",", "")
    subword   = temp[2].replace(",", "")
    idsubword = temp[3].replace("\n", "").replace(",", "").replace(" ", "").strip()



    labelled_train_dict[idsubword] = {}
    labelled_train_dict[idsubword]['recall'] = recall
    labelled_train_dict[idsubword]['subword'] = subword

    print(idsubword)
    print(labelled_train_dict[idsubword])
    
    

print(len(labelled_train_dict))
input()

f_7090.close()


#####################################################

f_out = open("context_merged_recalls_embeddings.txt", "w")

f = open("250kContextAllSubwordEmbeddings.txt", 'r')


jj = 0
for line in f.readlines():
    
    temp = line.split('\t')
   
    embeddings = temp[2]
    idsubword  = temp[0]
    subword    = temp[1]

    embeddings = embeddings.replace('\n', '')

    subword = subword.replace(",", "")

    idsubword = idsubword.replace(",", "")
    idsubword = idsubword.replace(" ", "")
    idsubword = idsubword.strip()

   
    list_embeddings_features = embeddings.split(',')

    print('*****************')
    print(len(list_embeddings_features))
    print(subword)
    print(idsubword)
    jj = jj + 1
    print(jj)
    

    the_row_type = 'test'
    the_recall   = '0.0'
    if idsubword in labelled_train_dict.keys():
        the_recall   = labelled_train_dict[idsubword]['recall']
        the_row_type = 'train'

        print(labelled_train_dict[idsubword]['subword'])
        
    ## input()

    list_markers = [the_row_type, the_recall, str(idsubword), subword]
    super_list_comb = list_markers + list_embeddings_features
    the_string_all = ','.join(super_list_comb)

    the_string_all = the_string_all + '\n'

    f_out.write(the_string_all)
    

f.close()
f_out.close()

print(jj)


print('<<<<<<DONE>>>>>>>')


