import os

file_path = os.path.join('C:\\', 'Users', 'ronnv', 'Desktop', 'myassessment.txt')

f = open(file_path, 'w')

def property_tax():
  tax = (ass/100) *.72
  return tax

def assessment_value(property_value):
  assessment = property_value * .60
  return assessment

try:
  property_value = float(input('Enter property value:'))
  ass = assessment_value(property_value)
except ValueError:
    print('Could not compute with given values.')
except ZeroDivisionError:
    print('Negative number entered. Not cool.')



print('Your assessment value is: %.2f' % assessment_value(property_value))
print('Your property tax is: %.2f' %property_tax())

f.write('Your assessment value is: %.2f\n' % assessment_value(property_value))
f.write('Your property tax is: %.2f' %property_tax())
f.close()