
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {'id': self._generateId(), 'first_name': 'John', 'last_name': 'Jackson', 'age': 33, 'lucky_numbers': [7, 13, 22]},
            {'id': self._generateId(), 'first_name': 'Jane', 'last_name': 'Jackson', 'age': 35, 'lucky_numbers': [10, 14, 3]},
            {'id': self._generateId(), 'first_name': 'Jimmy', 'last_name': 'Jackson', 'age': 5, 'lucky_numbers': [1]}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if 'id' not in member:
            member['id'] = self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        original_len = len(self._members) 
        self._members = [member for member in self._members if member['id'] != id]
        return len(self._members) < original_len

    def get_member(self, id):
        return next((member for member in self._members if member['id'] == id), None)

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
