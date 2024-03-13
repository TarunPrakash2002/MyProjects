import requests
import hashlib
import sys

#To request all API passwords from the URL
def req_api_data(hash_char): #hash_char-first 5 letters of hashed code
    url = 'https://api.pwnedpasswords.com/range/' + hash_char
    res = requests.get(url)
    if res.status_code != 200: #200-encoded, above 200-unsafe
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again!')
    return res

#To check number of passwords hacks/leaks
def passleak_count(hashes, passtail): #hashes-response, passtail-remaining char of hash code
    hashes = (line.split(':') for line in hashes.text.splitlines()) #to split the response as tail code and leak count
    for h,count in hashes: #h-tail of hash code, count-leak count
        if h == passtail: #to check if h is same as our password tail
            return count #to return the count of our actual password leak count
    return 0

#To check if our password is safe/unsafe
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #to hash using sha1, encode, convert to hexadecimal and to uppercase our password
    first5, tail = sha1password[:5], sha1password[5:]
    resp = req_api_data(first5)
    return passleak_count(resp, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times, change password')
        else:
            print(f'{password} was not found, all good!')
    return 'password check done'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
