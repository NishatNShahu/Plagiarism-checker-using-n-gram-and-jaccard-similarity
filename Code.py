#function to create n-grams

def get_ngrams(text, n):
    words = text.split()
    ngrams = [tuple(words[i:i+n]) for i in range(len(words) - n + 1)]
    return set(ngrams)

#function to calculate jaccard similarity

def jaccard_similarity(text1, text2, n=3):
    ngrams1 = get_ngrams(text1, n)
    ngrams2 = get_ngrams(text2, n)

    intersection = len(ngrams1.intersection(ngrams2))
    union = len(ngrams1.union(ngrams2))

    similarity = intersection / union 
    return similarity

#function to read from the given input file.

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
if __name__ == "__main__":
    
    file1_path = "f1.txt"
    file2_path = "f2.txt"

    text1 = read_text_from_file(file1_path)
    text2 = read_text_from_file(file2_path)
    
#Calling jaccard_similarity function.

similarity = jaccard_similarity(text1, text2, n=3)
    
print(f"Jaccard Similarity: {similarity}")
if similarity > 0.4:
    print("The texts are similar.Percentage:",similarity*100)
    print("plagiarism detected.")
else:
    print("The texts are not very similar. Similarity Percentage: ",similarity*100)
    print("Plagiarism not detected :)")

//code to plot graph//

import matplotlib.pyplot as plt

 #Plotting graph based on plagiarism detected or not.

def plot_similarity_graph(similarity, file_name,plagiarism_detected):
    labels = ['Similarity']
    percentages = [similarity * 100]

    colors = ['Red' if plagiarism_detected else 'Green' for _ in labels]

    # Plotting
    plt.bar(labels, percentages, color=colors)
    plt.title(f'Similarity Comparison for {file_name}')
    plt.xlabel('Files')
    plt.ylabel('Percentage')
    plt.ylim(0, 100)
    plt.show()

if __name__ == "__main__":
    file1_path = "f1.txt"
    file2_path = "f2.txt"
    
    text1 = read_text_from_file(file1_path)
    text2 = read_text_from_file(file2_path)
    similarity = jaccard_similarity(text1, text2, n=3)
    
    file2_path = "f2.txt"
    text2 = read_text_from_file(file2_path)
    similarity = jaccard_similarity(text1, text2, n=3)

    # Determine plagiarism detection
    plagiarism_detected = similarity > 0.4  # Adjust threshold as needed

    # Plotting graph for similarities with color indication
    plot_similarity_graph(similarity, "f1.txt", plagiarism_detected)
