print [0] * 10
print ', '.join(['justin', 'caterpillar', 'openhome'])
print list('justin')

admins = {'Justin', 'caterpillar'}
users = {'momor', 'hamini', 'Justin'}
print 'Justin' in admins
print admins & users
print admins | users
print admins - users
print admins ^ users

passwords = {'Justin' : 123456, 'caterpillar' : 933933}
print passwords['Justin']
passwords['Hamimi'] = 970221
print passwords
del passwords['caterpillar']
print passwords
print passwords.items()
print passwords.keys()
print passwords.values()

