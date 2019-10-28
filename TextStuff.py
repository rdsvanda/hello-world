course = 'Python for Beginners'
what = 'a Message for your clarity 1'
print(course.upper())
print(course.lower())

print(course.find('f'))
new_course = course.replace('Beginners', 'Super Beginners!')
print(new_course)
print(new_course.upper())
print(new_course.lower())

message = f' The first message is some crazy stuff.  Check it out {course} whoaaaa check out the second as well! {new_course}'
print(message)
print(message.upper())
print(message.lower())
new_message0 = (message.replace('s', 'Z'))
new_message1 = (new_message0.replace('m', '4'))
new_message2 = (new_message1.replace('o', 'p'))
new_message3 = (new_message2.replace('n', 'X'))

print(new_message0)
#print(what)
print(new_message1)

print(what)

print(new_message3)

print(message.upper())

print('Python' in new_message3)