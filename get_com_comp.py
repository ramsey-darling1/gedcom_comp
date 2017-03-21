# This is a simple script that will extract the surnames from two GEDCOMS and print any surnames that are found in both GEDCOMS

def get_com_comp_main():
    r1 = []
    r2 = []
    with open('one.ged') as f1:
        l1 = f1.readlines()
    if l1:
        for l in l1:
            if l[2:6] == 'NAME':
                x = l.split('/')
                if len(x) == 3:
                    if x[1] not in r1:
                        r1.append(x[1])
    else:
        print 'First GEDCOM not found'

    with open('two.ged') as f2:
        l2 = f2.readlines()
    if l2:
        for l in l2:
            if l[2:6] == 'NAME':
                x = l.split('/')
                if len(x) == 3:
                    if x[1] not in r2:
                        r2.append(x[1])
    else:
        print 'Second GEDCOM not found'

    if r1 and r2:
        if len(r1) >= len(r2):
            big_one = r1
            small_one = r2
        else:
            big_one = r2
            small_one = r1
        for surname in big_one:
            if surname in small_one:
                print surname
    else:
        print 'Sorry, there was an error parsing one or both GEDCOMs'
    return


#run the function:
get_com_comp_main()
