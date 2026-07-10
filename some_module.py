def main():
    print('Ran directly from the script')



if __name__ == '__main__':
    main()
else:
    print(f'{__name__}.py is running externally from another script')