# write your code here
person={
    'name':'msaeid',
    'age':'20',
    'hobbiesss':['hores riding','runing','swiming']
}
print(person['name'])
print(person['age'])


person['age']=21
person['country']='kuwait'
print(person)
print(len(person))
person['hobbiesss'].append('reding')

print(person['hobbiesss'])
print(len(person['hobbiesss']))


def check_hobby(person):
    if len(person['hobbiesss']) >= 3:
        print('you are amazing')

check_hobby(person)