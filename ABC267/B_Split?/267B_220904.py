def main():
    s = list(input())
    col_stat = [
        s[6] == "1",
        s[3] == "1", 
        s[7] == "1" or s[1] == "1",
        s[4] == "1" or s[0] == "1", 
        s[8] == "1" or s[2] == "1", 
        s[5] == "1", 
        s[9] == "1"
    ]


    # Marker
    
    if s[0] == "1":
        print("No")
        return 
    else:
        for i in range(7):
            for j in range(i):
                if col_stat[i] and col_stat[j]:
                    for x in range(j+1, i):
                        if not col_stat[x]:
                            print("Yes")
                            return  

    print("No")
    return


if __name__ == "__main__":
    main()
    
    
