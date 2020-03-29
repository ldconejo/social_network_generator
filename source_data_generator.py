'''
Takes a list of names and a list of last names and creates a number of combinations
with a unique user_id, name, last_name and email.
'''
import random
import csv
import argparse
import pysnooper

def parse_cmd_arguments():
    """Ingest arguments into an object."""
    parser = argparse.ArgumentParser(description='Generates random accounts and status updates for a simulated social network.')
    parser.add_argument('-nf', '--names_file', help='list of names', default='names.txt', required=False)
    parser.add_argument('-ln', '--last_names_file', help='list of last names', default='last_names.txt',
                        required=False)
    parser.add_argument('-n', '--nouns_file', help='list of nouns', default='nouns.txt', required=False)
    parser.add_argument('-a', '--adjectives_file', help='list of adjectives', default='adjectives.txt',
                        required=False)
    parser.add_argument('-v', '--verbs_file', help='list of verbs', default='verbs.txt', required=False)
    parser.add_argument('-af', '--accounts_file', help='user account file', default='accounts.csv',
                        required=False)
    parser.add_argument('-sf', '--status_file', help='status file', default='status_updates.csv',
                        required=False)
    parser.add_argument('-na', '--number_of_accounts', help='number of accounts to create',
                        default=100, required=False)
    parser.add_argument('-ns', '--number_of_status', help='number of status to create',
                        default=1000, required=False)

    return parser.parse_args()

def load_values(names_file, last_names_file, names_list, last_names_list):
    '''
    Loads the values from the source files into lists
    '''
    with open(names_file, newline='') as names:
        for name in names:
            names_list.append(name.strip())

    with open(last_names_file, newline='') as last_names:
        for last_name in last_names:
            last_names_list.append(last_name.strip())

def create_user_accounts(names_list, last_names_list, target, email_providers, output_file,
                         user_dict):
    '''
    Creates a total of target unique user accounts
    with user_id, name, last_name and email
    '''
    total_created = 0
    while total_created < target:
        name = random.choice(names_list)
        last_name = random.choice(last_names_list)
        # Adding a random integer to make it easier to have
        # unique names.
        rand_number = random.randint(1,99)
        user_id = f"{name}.{last_name}{rand_number}"
        if user_id not in user_dict:
            email_provider = random.choice(email_providers)
            email = f"{name}.{last_name}{rand_number}@{email_provider}"
            user_dict[user_id] = {
                'user_id' : user_id,
                'name' : name,
                'last_name' : last_name,
                'email' : email
            }
            total_created += 1

    # Save to csv
    with open(output_file, mode='w') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        file_writer.writerow(['USER_ID', 'EMAIL', 'NAME', 'LASTNAME'])
        # Iterate through the collection of users
        for user in user_dict.values():
            file_writer.writerow(([user['user_id'], user['name'], user['last_name'],
                                   user['email']]))

def create_phrases(nouns_file, verbs_file, adjectives_file, nouns_list, verbs_list, adjectives_list,
                   user_dict, phrase_dict, output_file, target):
    '''
    Creates random phrases
    '''
    with open(nouns_file, newline='') as nouns:
        for noun in nouns:
            nouns_list.append(noun.strip())

    with open(verbs_file, newline='') as verbs:
        for verb in verbs:
            verbs_list.append(verb.strip())

    with open(adjectives_file, newline='') as adjectives:
        for adjective in adjectives:
            adjectives_list.append(adjective.strip())

    total_phrases = 0
    while total_phrases < target:
        new_phrase = f"{random.choice(adjectives_list)} {random.choice(nouns_list)} {random.choice(verbs_list)} {random.choice(adjectives_list)} {random.choice(nouns_list)}"

        # Select a random user for user_dict
        user_id = random.choice(list(user_dict.keys()))

        # Create a random status_id
        status_id = f"{user_id}_{random.randint(0, 1000)}"
        while status_id in phrase_dict:
            user_id = random.choice(list(user_dict.keys()))
            status_id = f"{user_id}_{random.randint(0, 500)}"

        phrase_dict[status_id] = {
            'status_id' : status_id,
            'user_id' : user_id,
            'status_text' : new_phrase
        }
        total_phrases += 1

    # Save to csv
    with open(output_file, mode='w') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        file_writer.writerow(['STATUS_ID','USER_ID', 'STATUS_TEXT'])
        # Iterate through the collection of status
        for status in phrase_dict.values():
            file_writer.writerow(([status['status_id'], status['user_id'], status['status_text']]))


if __name__ == '__main__':
    ARGS = parse_cmd_arguments()
    names_list = []
    last_names_list = []
    user_dict = {}
    # Making up random email providers
    EMAIL_PROVIDERS = ('funmail.com', 'goodmail.com', 'testmail.com')
    load_values(ARGS.names_file, ARGS.last_names_file, names_list, last_names_list)
    create_user_accounts(names_list, last_names_list, int(ARGS.number_of_accounts), EMAIL_PROVIDERS, ARGS.accounts_file,
                         user_dict)

    # Now create status entries
    nouns_list = []
    verbs_list = []
    adjectives_list = []
    phrase_dict = {}
    create_phrases(ARGS.nouns_file, ARGS.verbs_file, ARGS.adjectives_file, nouns_list, verbs_list,
                   adjectives_list, user_dict, phrase_dict, ARGS.status_file, int(ARGS.number_of_status))
