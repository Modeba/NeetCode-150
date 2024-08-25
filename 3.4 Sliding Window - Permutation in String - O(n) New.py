s1 = "ab"
s2 = "eidbaooo"

def checkInclusion(s1, s2):
    # If s2 is shorter than it can not contain S1
    if len(s2) < len(s1):
        return False

    # Map s1 and the same length substring of s2
    counts1 = [0 for _ in range(26)]
    counts2 = [0 for _ in range(26)]
    for i in range(len(s1)):
        counts1[ord(s1[i]) - ord('a')] += 1
        counts2[ord(s2[i]) - ord('a')] += 1

    # 'Move' forward the s1 sized substring in s2 by adding
    # characters on the right and removing on the left
    for r in range(len(s1), len(s2)):
        if counts1 == counts2:
            return True
        counts2[ord(s2[r]) - ord('a')] += 1
        counts2[ord(s2[r - len(s1)]) - ord('a')] -= 1
    
    return counts1 == counts2

print(checkInclusion(s1, s2))