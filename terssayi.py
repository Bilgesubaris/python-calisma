def ters(sayi):
  if sayi < 0:
    return 0

  return str(sayi)[::-1]

def main():
  print(ters(123))

if __name__ == "__main__":
  main()
