def count_a_occurrences(s):

    # Convertemos a string para minúscula para facilitar a contagem
    s_lower = s.lower()
    # Contagem de vezes que a letra 'a' aparece na string 
    count = s_lower.count('a')
    return count

def main():
    input_string = input("Digite uma string para verificar a ocorrência da letra 'a': ")
    
    # Conta o número de ocorrências da letra 'a'
    occurrences = count_a_occurrences(input_string)
    
    if occurrences > 0:
        print(f"A letra 'a' (maiúscula ou minúscula) ocorre {occurrences} vezes na string.")
    else:
        print("A letra 'a' não ocorre na string.")

if __name__ == "__main__":
    main()
