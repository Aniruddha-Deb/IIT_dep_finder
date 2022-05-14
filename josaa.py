# A mock implementation of the JoSAA seat allocation algorithm, taking into 
# account categories, reservations and all the nuances involved in allocating
# students.
#
# References:
# 1. Joint Seat Allocation 2018: An algorithmic perspective. 
#    https://arxiv.org/pdf/1904.06698.pdf
#

from collections import deque
from bisect import insort
import heapq

# program is of the form
# program = {
#   'code': 
#   'num_seats':
#   'merit_list': 
# }
#
# candidate is of the form
# candidate = {
#   'roll_no': 
#   'pref_list': 
# }

def reject(x, Q, prefidx):
    prefidx[x['roll_no']] += 1
    if len(x['pref_list']) > prefidx[x['roll_no']]:
        deque.append(Q, x)

def basic_allocation(programs, candidates):

    waitlist = {program['code']:[] for program in programs}
    prefidx = {x['roll_no']:0 for x in candidates}
    Q = deque()
    for candidate in candidates:
        if candidate['pref_list']:
            deque.append(Q,candidate)

    while Q:
        x = deque.popleft(Q)
        p = x['pref_list'][prefidx[x['roll_no']]]
        rank_x = p['merit_list'][x['roll_no']] 
        pcode = p['code']
        if x['roll_no'] not in p['merit_list'].keys():
            reject(x, Q, prefidx)
            continue
        if len(waitlist[pcode]) == p['num_seats']:
            (rank_y,y) = waitlist[pcode][-1]
            if rank_x < rank_y:
                waitlist[pcode].pop()
                reject(y, Q, prefidx)
                insort(waitlist[pcode], (rank_x,x))
            else:
                reject(x, Q, prefidx)
        else:
            insort(waitlist[pcode], (rank_x,x))

    matches = {}

    for x in candidates:
        if len(x['pref_list']) > prefidx[x['roll_no']]:
            matches[x['roll_no']] = x['pref_list'][prefidx[x['roll_no']]]['code']
        else:
            matches[x['roll_no']] = None

    return (matches, waitlist)

def gale_shapley(suitors, suitees):
    matching = dict.fromkeys(suitors,None)
    idxs = dict.fromkeys(suitors,0)

    proposal_pool = {k:[] for k in suitees.keys()}
    rno = 1
    while None in matching.values():
        unmatched_suitors = [s for s in suitors if not matching[s]]
        for suitor in unmatched_suitors:
            suitee = suitors[suitor][idxs[suitor]]
            proposal_pool[suitee].append(suitor)

        print(f"R{rno} Proposal pool: {proposal_pool}")

        proposed_suitees = [s for s in suitees if proposal_pool[s]]
        for suitee in proposed_suitees:
            match_idx = min([suitees[suitee].index(s) for s in proposal_pool[suitee]])
            match_suitor = suitees[suitee][match_idx]
            while proposal_pool[suitee]:
                suitor = proposal_pool[suitee].pop()
                if suitor == match_suitor:
                    matching[suitor] = suitee
                idxs[suitor] += 1

        rno += 1

    return matching

def gale_shapley_test():
   
    m = int(input())
    n = int(input())
    M = dict(zip(range(1,m+1),[[int(i) for i in input().split(" ")] for j in range(m)]))
    N = dict(zip(range(1,n+1),[[int(i) for i in input().split(" ")] for j in range(n)]))

    print(M)
    print(N)

    print(gale_shapley(M,N))

def main():
    # reading course codes and generating some dummy data...
    # Hm, how _do_ we generate dummy data?
    #
    # course codes atleast can be taken from the JoSAA site.
    # I'll refer to the JEE2019 Data for other inspiration
    #
    # for a first approximation, have a clear ranking of departments (somewhat
    # similar to what we have now),

    candidates = []
    programs = {}
    meritlist = {}

    with open("programs.txt", "r") as progs:
        for l in progs:
            A = [int(i) for i in l.split(",")]
            programs[A[0]] = {
                'code': A[0],
                'num_seats': A[1],
                'merit_list': meritlist
            }

    with open("data.txt","r") as data:
        for l in data:
            A = [int(i) for i in l.split(",")]
            candidates.append({'roll_no': A[0], 'pref_list': [programs[i] for i in A[2:]]})
            meritlist[A[0]] = A[1]

    print(basic_allocation(programs.values(),candidates)[0])

if __name__ == "__main__":
    main()
