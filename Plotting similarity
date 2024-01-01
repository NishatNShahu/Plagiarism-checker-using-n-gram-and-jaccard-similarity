//Code to plot the graph of similarity between file 1 and other files. 

import matplotlib.pyplot as plt

def plot_similarity_graph(similarity1, similarity2, similarity3, similarity4, file_name, plagiarism_detected1, plagiarism_detected2, plagiarism_detected3, plagiarism_detected4):
    """Plotting graph based on plagiarism detected or not."""
    labels = ['Similarity1', 'Similarity2', 'Similarity3', 'Similarity4']
    percentages = [similarity1 * 100, similarity2 * 100, similarity3 * 100, similarity4 * 100]

    colors = ['Red' if plagiarism_detected else 'Green' for plagiarism_detected in [plagiarism_detected1, plagiarism_detected2, plagiarism_detected3, plagiarism_detected4]]

    # Plotting
    plt.bar(labels, percentages, color=colors)
    plt.title(f'Similarity Comparison for {file_name}')
    plt.xlabel('Files')
    plt.ylabel('Percentage')
    plt.ylim(0, 100)
    plt.show()

if __name__ == "__main__":
    
    file1_path = "f1.txt"
    text1 = read_text_from_file(file1_path)
    
    file2_path = "f2.txt"
    text2 = read_text_from_file(file2_path)
    similarity1 = jaccard_similarity(text1, text2, n=3)
    print(f"Jaccard Similarity 2: {similarity1*100}")
        
    file3_path = "f3.txt"
    text3 = read_text_from_file(file3_path)
    similarity2 = jaccard_similarity(text1, text3, n=3)
    print(f"Jaccard Similarity 3: {similarity2*100}")
    
    file4_path = "f4.txt"
    text4 = read_text_from_file(file4_path)
    similarity3 = jaccard_similarity(text1, text4, n=3)
    print(f"Jaccard Similarity 4: {similarity3*100}")
    
    file5_path = "f5.txt"
    text5 = read_text_from_file(file5_path)
    similarity4 = jaccard_similarity(text1, text5, n=3)
    print(f"Jaccard Similarity 5: {similarity4*100}")

    # Determine plagiarism detection
    plagiarism_detected1 = similarity1 > 0.4
    plagiarism_detected2 = similarity2 > 0.4
    plagiarism_detected3 = similarity3 > 0.4
    plagiarism_detected4 = similarity4 > 0.4  # Adjust threshold as needed

    # Plotting graph for similarities with color indication
    plot_similarity_graph(similarity1, similarity2, similarity3, similarity4, "f1.txt", plagiarism_detected1, plagiarism_detected2, plagiarism_detected3, plagiarism_detected4)
