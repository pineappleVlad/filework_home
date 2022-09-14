def file_operation():
    with open("1.txt", encoding="utf-8") as f1, open("2.txt", encoding="utf-8") as f2, open("3.txt", encoding="utf-8") as f3, open("4.txt", "w", encoding="utf-8") as f4:
        count_1 = 0
        text_1 = []
        for line in f1:
            count_1 += 1
            text_1.append(line.strip())
        
        count_2 = 0
        text_2 = []
        for line in f2:
            count_2 += 1
            text_2.append(line.strip())

        count_3 = 0
        text_3 = []
        for line in f3:
            count_3 += 1
            text_3.append(line.strip())

        if count_1 > count_2 and count_1 > count_3:
            f4.write(f"1.txt\n{count_1}\n")
            for a in text_1:
                f4.write(f"{a}\n")
            if count_2 > count_3:
                f4.write(f"2.txt\n{count_2}\n")
                for b in text_2:
                    f4.write(f"{b}\n")
                f4.write(f"3.txt\n{count_3}\n")
                for c in text_3:
                    f4.write(f"{c}\n")
            else:
                f4.write(f"3.txt\n{count_3}\n")
                for c in text_3:
                    f4.write(f"{c}\n")
                f4.write(f"2.txt\n{count_2}\n")
                for b in text_2:
                    f4.write(f"{b}\n")
        elif count_2 > count_1 and count_2 > count_3:
            f4.write(f"2.txt\n{count_1}\n")
            for a in text_2:
                f4.write(f"{a}\n")
            if count_1 > count_3:
                f4.write(f"1.txt\n{count_1}\n")
                for b in text_1:
                    f4.write(f"{b}\n")
                f4.write(f"3.txt\n{count_3}\n")
                for c in text_3:
                    f4.write(f"{c}\n")
            else:
                f4.write(f"3.txt\n{count_3}\n")
                for c in text_3:
                    f4.write(f"{c}\n")
                f4.write(f"1.txt\n{count_1}\n")
                for b in text_1:
                    f4.write(f"{b}\n")
        elif count_3 > count_1 and count_3 > count_2:
            f4.write(f"3.txt\n{count_3}\n")
            for a in text_3:
                f4.write(f"{a}\n")
            if count_2 > count_1:
                f4.write(f"2.txt\n{count_2}\n")
                for b in text_2:
                    f4.write(f"{b}\n")
                f4.write(f"1.txt\n{count_1}\n")
                for c in text_1:
                    f4.write(f"{c}\n")
            else:
                f4.write(f"1.txt\n{count_1}\n")
                for c in text_1:
                    f4.write(f"{c}\n")
                f4.write(f"2.txt\n{count_2}\n")
                for b in text_2:
                    f4.write(f"{b}\n")
            


file_operation()
