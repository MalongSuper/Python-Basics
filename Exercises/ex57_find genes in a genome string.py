# 57. Find Genes in a Genome String

def valid_gene(gene):
    valid_list = ['A', 'C', 'G', 'T']
    gene_list = list(gene)

    for gen in range(len(gene_list)):
        if gene_list[gen] not in valid_list:
            return False

    return True


def len_of_string(gene):
    gene_list = list(gene)

    if len(gene_list) % 3 != 0:
        return False

    return True


def separated_gene(gene):
    gene_list = list(gene)
    end_gene = ['ATG', 'TAG', 'TAA', 'TGA']
    gene_string = ''.join(gene_list)

    # Find value 'ATG'
    start_gene = gene_string.find('ATG')

    # Use loop to indicate value in the list of gene
    while start_gene != -1:  # The loop ends when reaching index -1
        # Indicate value after 'ATG'
        start_list = gene[start_gene+3:]

        for end in range(0, len(start_list), 3):
            # Display all the values after 'ATG'
            end_list = start_list[end:end+3]

            # Until reaching the value being in the end_list
            if end_list in end_gene:
                break

            print(end_list, end=" ")

        # Continue to find the value 'ATG'
        start_gene = gene.find('ATG', start_gene+1)


'''
Some sample inputs
- Length 9: ATGCATGCA
- Length 12: ATGCCTAGCTAG
- Length 15: ATGGCTACCGGATAA
'''

gene = str(input('Enter a Genome String: '))

if not valid_gene(gene):
    print("Error: The Genome String is Invalid.")
elif not len_of_string(gene):
    print("Error: The Genome String must have the length be divisible by 3.")
else:
    print("Gene Found:", end=" ")
    separated_gene(gene)
