a = [1, 2, 3, 1, 2, 3]

def selection_sort(a):
   p = 0
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j = j + 1
      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp
      i = i + 1

def main(a):
   selection_sort(a)
   print a

if __name__ == "__main__":
   main(a)
