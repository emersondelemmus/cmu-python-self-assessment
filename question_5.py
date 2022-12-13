## Given the following dictionary:

applicant = {"id": 10348,
             "fname": "John",
             "lname": "Smith",
             "city": "NYC"}
# Which of the following statements will return the applicant’s fname value? Select all that apply.

#print(applicant[1])
print(applicant.get('fname'))
print(applicant['fname'])
print(applicant.pop('fname'))