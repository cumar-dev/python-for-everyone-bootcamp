greeting = input("what is your name ? ");
print("Hello welcome Mr:", greeting);

correct = 0;
wrong = 0;
Quiz1 = input("sheeg caasimada soomaaliya ? ");
Quiz2 = input("sheeg caasimada gobolka shabeelada hoose ? ");
Quiz3 = input("sheeg caasimada gobolka bari ? ");
Quiz4 = input("sheeg caasimada gobolka baay ? ");

if Quiz1.lower() == "mogadisho" :
    print("jawaabtadu 1aad waa sax");
    correct +=1;
else:
    print("jawaabtaadu waa khalad");
    wrong +-1;

if Quiz2.lower() == "marko":
     print("jawaabtadu 2aad waa sax");
     correct +=1;
else:
    print("jawaabtaadu waa khalad");
    wrong +-1;

if Quiz3.lower() == "boosaaso":
     print("jawaabtadu 3aad waa sax");
     correct +=1;
else: 
    print("jawaabtu waa khalad");
    wrong -=1;

if Quiz4.lower() == "baydhabo":
     print("jawaabtadu 4aad waa sax");
     correct +=1;
else: 
    print("jawaabtu waa khalad");
    wrong -=1;

print(greeting, "waxaad saxday", correct, "suaal", "waxaad khaladay", wrong, "suaal");