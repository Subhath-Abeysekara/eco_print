from common import format_docs
from service import connect_instructions
collection = connect_instructions()

def get_instruction():
    instructions = collection.find()
    response = {
        "instructions": format_docs(instructions)
    }
    return response