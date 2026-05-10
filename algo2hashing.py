# Names: Ivy Loi, Homan Qiu, Robert Gutierrez, Richie Nguyen
# Emails: iloi05@csu.fullerton.edu, hqiu2006@csu.fullerton.edu, lil.rjg3@csu.fullerton.edu, richienguyen@csu.fullerton.edu
# CPSC 335 section 11
# Project 4: Algorithm 2
# Date: 5/8/2026

def detectDuplicates(ids, hashSize=13):
    # make a table to keep track of ids
    hashTable = [None for _ in range(hashSize)]
    # make a table to keep track of counts
    hashTableCount = [0 for _ in range(hashSize)]

    # looping through ids to insert into hash table
    for currentId in ids:
        # calculating the index
        index = currentId % hashSize
        
        # checking if the spot is taken by a different id (collision)
        if hashTable[index] is not None and hashTable[index] != currentId:
            # resize table and try again recursively
            return detectDuplicates(ids, hashSize * 2)

        # putting the id in the table
        hashTable[index] = currentId
        # adding to the count
        hashTableCount[index] += 1

    # tracking uniques and duplicates
    unique = 0
    duplicate = 0

    print("Duplicates found (in order of first appearance):")

    # looping through ids again to print in order
    for currentId in ids:
        # calculating the index
        index = currentId % hashSize

        # checking if it appears more than once
        if hashTableCount[index] > 1:
            print(str(hashTable[index]) + " -> appears " + str(hashTableCount[index]) + " times")
            # updating duplicate count
            duplicate += 1
            # setting count to 0 so we don't print it again
            hashTableCount[index] = 0  
            
        # checking if it appears exactly once
        elif hashTableCount[index] == 1:
            # updating unique count
            unique += 1
            # setting count to 0 so we don't count it again
            hashTableCount[index] = 0  
    
    print("\nTotal unique IDs: " + str(unique))
    print("Total duplicate IDs: " + str(duplicate))

def main():
    # attempting to read from file as required by instructions
    try:
        with open("sample_ids.txt", "r") as file:
            # getting contents and removing brackets
            content = file.read().strip().replace("[", "").replace("]", "")
            # turning strings into integers for the ids array
            ids = [int(x.strip()) for x in content.split(",") if x.strip()]
            
            print("File Input Results:")
            detectDuplicates(ids)
            
    except FileNotFoundError:
        # fallback example if file cannot be read
        print("Example 1 (Hardcoded Fallback):")
        ids = [1042, 2381, 1042, 5567, 2381, 8810, 1042, 3390, 5567]
        detectDuplicates(ids)

if __name__ == "__main__":
    main()